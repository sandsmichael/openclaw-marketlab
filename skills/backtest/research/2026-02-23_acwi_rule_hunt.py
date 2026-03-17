import os
import numpy as np, pandas as pd
from sqlalchemy import create_engine,text
from datetime import date

ENGINE_URI = os.getenv('MARKETLAB_DB_URI')
if not ENGINE_URI:
    raise RuntimeError('MARKETLAB_DB_URI is not set. Put credentials in /home/msands/.openclaw/workspace/.env')
engine=create_engine(ENGINE_URI)
out=f'/home/msands/.openclaw/workspace/skills/backtest/agentic/{date.today().isoformat()}_backtest_results.csv'
with engine.connect() as c:
    px=pd.read_sql(text('select date,ticker,adj_px from prices order by date'),c)
    macro=pd.read_sql(text('select date, "VIX_LVL" as vix, "CPI_YOY" as cpi, "FEDFUNDS_LVL" as fed from macro order by date'),c)
    syc=pd.read_sql(text('select date,yield_type,"10_yr" as y10,"2_yr" as y2 from sovereign_yield_curve where country=\'US\' order by date'),c)
px['date']=pd.to_datetime(px['date']); P=px.pivot(index='date',columns='ticker',values='adj_px').sort_index()
U=[x for x in ['SPY.US','IWF.US','IWD.US','IWM.US','IWO.US','EFA.US','EEM.US','MTUM.US','QUAL.US','USMV.US'] if x in P.columns]
R=P[U].pct_change(fill_method=None)
acwi=0.6*R['SPY.US'].fillna(0)+0.3*R['EFA.US'].fillna(0)+0.1*R['EEM.US'].fillna(0)
macro['date']=pd.to_datetime(macro['date']); M=macro.set_index('date').sort_index().reindex(R.index,method='ffill')
syc['date']=pd.to_datetime(syc['date']); Y=syc[syc['yield_type'].isin(['benchmark','par'])].sort_values('date').drop_duplicates('date').set_index('date')
slope=(Y['y10']-Y['y2']).reindex(R.index,method='ffill')
acwimom=((1+acwi).rolling(63).apply(np.prod,raw=True)-1)

sleeves={
 'growth':0.7*R.get('IWF.US',0).fillna(0)+0.3*R.get('IWO.US',0).fillna(0),
 'quality':0.7*R.get('QUAL.US',0).fillna(0)+0.3*R.get('USMV.US',0).fillna(0),
 'beta':0.8*R.get('SPY.US',0).fillna(0)+0.2*R.get('IWM.US',0).fillna(0),
 'intl':0.7*R.get('EFA.US',0).fillna(0)+0.3*R.get('EEM.US',0).fillna(0),
 'value':0.8*R.get('IWD.US',0).fillna(0)+0.2*R.get('IWM.US',0).fillna(0),
}

def perf(x):
    x=x.dropna()
    if len(x)<756:return None
    b=acwi.reindex(x.index).fillna(0)
    nav=(1+x).cumprod(); yrs=(x.index[-1]-x.index[0]).days/365.25
    cagr=nav.iloc[-1]**(1/yrs)-1; vol=x.std()*np.sqrt(252); sh=(x.mean()*252)/(vol+1e-12)
    ex=x-b; te=ex.std()*np.sqrt(252); ir=(ex.mean()*252)/(te+1e-12)
    dd=(nav/nav.cummax()-1).min()
    return cagr,sh,ex.mean()*252,ir,dd

rows=[]
rng=np.random.default_rng(7)
for _ in range(5000):
  vt=float(rng.choice([14,16,18,20,22,24]))
  st=float(rng.choice([-0.5,-0.25,0,0.25,0.5]))
  fd=float(rng.choice([3.5,4.0,4.5,5.0,5.5]))
  cp=float(rng.choice([2.0,2.5,3.0,3.5,4.0]))
  mm=float(rng.choice([-0.10,-0.05,0,0.05,0.1]))
  a,b=rng.choice([('growth','quality'),('beta','quality'),('growth','value'),('beta','intl')])
  tv=float(rng.choice([0.10,0.12,0.15,0.18,0.22]))
  cap=float(rng.choice([1.0,1.25,1.5,2.0,2.5,3.0]))

  on=((M['vix']<vt)&(slope>st)&(M['fed']<fd)&(M['cpi']<cp)&(acwimom>mm)).astype(float).shift(1).fillna(0)
  base=on*sleeves[a]+(1-on)*sleeves[b]
  rv=base.rolling(21).std()*np.sqrt(252)
  p=(tv/(rv+1e-12)).clip(0,cap).shift(1).fillna(0)*base
  stt=perf(p)
  if stt is None: continue
  cagr,sh,ex,ir,dd=stt
  rows.append({'Strategy':f'RULE_v{vt}_s{st}_f{fd}_c{cp}_m{mm}_{a}_{b}_tv{tv}_cap{cap}','Benchmark':'MSCI ACWI proxy (60/30/10)','Description':'Econometric threshold regime model using volatility, curve slope, policy rate, inflation and ACWI momentum; dynamic sleeve switch + vol target.','Signal_Calc':f'on if VIX<{vt}&slope>{st}&fed<{fd}&cpi<{cp}&acwi63m>{mm}; on->{a}, off->{b}; tv={tv}, cap={cap}','CAGR':cagr,'Sharpe':sh,'AnnExcessRet':ex,'InfoRatio':ir,'MaxDD':dd})

res=pd.DataFrame(rows).sort_values(['InfoRatio','Sharpe','AnnExcessRet'],ascending=[False,False,False]).reset_index(drop=True)
res.to_csv(out,index=False)
hit=res[(res['AnnExcessRet']>=0.01)&(res['Sharpe']>1.0)]
print('N',len(res),'HITS',len(hit))
print((hit if len(hit) else res).head(20)[['Strategy','Sharpe','AnnExcessRet','InfoRatio','CAGR','MaxDD']].to_string(index=False))