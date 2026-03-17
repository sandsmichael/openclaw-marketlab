import os
import numpy as np
import pandas as pd
from sqlalchemy import create_engine, text
from datetime import date

ENGINE_URI=os.getenv('MARKETLAB_DB_URI')
if not ENGINE_URI:
    raise RuntimeError('MARKETLAB_DB_URI is not set. Put credentials in /home/msands/.openclaw/workspace/.env')
OUT=f'/home/msands/.openclaw/workspace/skills/backtest/agentic/{date.today().isoformat()}_backtest_results.csv'

engine=create_engine(ENGINE_URI)
with engine.connect() as c:
    px=pd.read_sql(text('select date,ticker,adj_px from prices order by date'),c)
    macro=pd.read_sql(text('select date, "VIX_LVL" as vix, "CPI_YOY" as cpi, "FEDFUNDS_LVL" as fed from macro order by date'),c)
    syc=pd.read_sql(text('select date,yield_type,"10_yr" as y10,"2_yr" as y2 from sovereign_yield_curve where country=\'US\' order by date'),c)

px['date']=pd.to_datetime(px['date'])
P=px.pivot(index='date',columns='ticker',values='adj_px').sort_index()
U=[x for x in ['SPY.US','IWB.US','IWF.US','IWD.US','IWM.US','IWR.US','IWP.US','IWS.US','IWN.US','IWO.US','EFA.US','EEM.US','MTUM.US','QUAL.US','USMV.US','VLUE.US','SIZE.US'] if x in P.columns]
R=P[U].pct_change(fill_method=None)
acwi=0.6*R['SPY.US'].fillna(0)+0.3*R['EFA.US'].fillna(0)+0.1*R['EEM.US'].fillna(0)

macro['date']=pd.to_datetime(macro['date'])
M=macro.set_index('date').sort_index().reindex(R.index,method='ffill')
syc['date']=pd.to_datetime(syc['date'])
Y=syc[syc['yield_type'].isin(['benchmark','par'])].sort_values('date').drop_duplicates('date').set_index('date')
slope=(Y['y10']-Y['y2']).reindex(R.index,method='ffill')

mom={lb:P[U].pct_change(lb,fill_method=None) for lb in [21,63,126,252]}
vol={lb:R[U].rolling(lb).std()*np.sqrt(252) for lb in [21,63]}
reg=((M['vix']<20).astype(float)+(slope>0).astype(float)+(M['fed']<5).astype(float)+(M['cpi']<4).astype(float))


def perf(x):
    x=x.dropna()
    if len(x)<756:return None
    b=acwi.reindex(x.index).fillna(0)
    nav=(1+x).cumprod(); yrs=(x.index[-1]-x.index[0]).days/365.25
    cagr=nav.iloc[-1]**(1/yrs)-1
    vola=x.std()*np.sqrt(252)
    sharpe=(x.mean()*252)/(vola+1e-12)
    ex=x-b
    te=ex.std()*np.sqrt(252)
    ir=(ex.mean()*252)/(te+1e-12)
    dd=(nav/nav.cummax()-1).min()
    return dict(CAGR=float(cagr),Vol=float(vola),Sharpe=float(sharpe),AnnExcessRet=float(ex.mean()*252),InfoRatio=float(ir),MaxDD=float(dd),obs_days=int(len(x)),start=str(x.index[0].date()),end=str(x.index[-1].date()))

rows=[]
# random econometric search
rng=np.random.default_rng(42)
combos=120
for i in range(combos):
    m1=int(rng.choice([21,63,126,252]))
    m2=int(rng.choice([21,63,126]))
    vb=int(rng.choice([21,63]))
    w=rng.dirichlet([2,2,2])
    w1,w2,wv=float(w[0]),float(w[1]),float(w[2])*1.5
    k=int(rng.choice([1,2,3,4]))
    rg=int(rng.choice([1,2,3]))
    tv=float(rng.choice([0.10,0.12,0.15,0.18]))
    cap=float(rng.choice([1.0,1.25,1.5,2.0]))
    cth=float(rng.choice([0,0.00005,0.0001,0.0002]))

    score=w1*mom[m1]+w2*mom[m2]-wv*vol[vb]
    me=score.resample('ME').last()
    wgt=pd.DataFrame(0.0,index=me.index,columns=U)
    for dt,row in me.iterrows():
        s=row.dropna().sort_values(ascending=False)
        if len(s)<k: continue
        if s.iloc[0]<=cth: continue
        wgt.loc[dt,s.index[:k]]=1.0/k
    wd=wgt.shift(1).reindex(R.index,method='ffill').fillna(0)
    base=(wd*R.fillna(0)).sum(axis=1)
    gated=base.where(reg.shift(1)>=rg,0.0)
    rv=gated.rolling(21).std()*np.sqrt(252)
    lev=(tv/(rv+1e-12)).clip(0,cap)
    port=lev.shift(1).fillna(0)*gated
    st=perf(port)
    if st:
        rows.append({'Strategy':f'RAND_COMP_{i}','Benchmark':'MSCI ACWI proxy (60/30/10)','Description':'Randomized econometric composite of momentum/volatility with macro regime gate + vol targeting','Signal_Calc':f'score={w1:.3f}*mom{m1}+{w2:.3f}*mom{m2}-{wv:.3f}*vol{vb}; top{k} monthly; cash if score<{cth}; regime>={rg}; tv={tv}, cap={cap}',**st})

# deterministic regime models
sleeves={
 'growth':0.6*R.get('IWF.US',0).fillna(0)+0.4*R.get('IWO.US',0).fillna(0),
 'value':0.6*R.get('IWD.US',0).fillna(0)+0.4*R.get('IWN.US',0).fillna(0),
 'quality':0.7*R.get('QUAL.US',0).fillna(0)+0.3*R.get('USMV.US',0).fillna(0),
 'beta':0.7*R.get('SPY.US',0).fillna(0)+0.3*R.get('IWM.US',0).fillna(0),
}
for vt in [16,18,20,22]:
  for stp in [-0.25,0,0.25,0.5]:
    on=((M['vix']<vt)&(slope>stp)).astype(float).shift(1).fillna(0)
    for a,b in [('growth','quality'),('beta','quality'),('growth','value')]:
      base=on*sleeves[a]+(1-on)*sleeves[b]
      for tv in [0.10,0.12,0.15,0.18]:
        for cap in [1.0,1.25,1.5,2.0]:
          rv=base.rolling(21).std()*np.sqrt(252)
          port=(tv/(rv+1e-12)).clip(0,cap).shift(1).fillna(0)*base
          st=perf(port)
          if st:
            rows.append({'Strategy':f'REGIME_v{vt}_s{stp}_{a}_{b}_tv{tv}_cap{cap}','Benchmark':'MSCI ACWI proxy (60/30/10)','Description':'VIX+yield-curve econometric regime switch among sleeves with vol targeting','Signal_Calc':f'if VIX<{vt} and slope>{stp} hold {a} else {b}; tv={tv}, cap={cap}',**st})

res=pd.DataFrame(rows).sort_values(['InfoRatio','Sharpe','AnnExcessRet'],ascending=[False,False,False]).reset_index(drop=True)
res.to_csv(OUT,index=False)
hit=res[(res['AnnExcessRet']>=0.01)&(res['Sharpe']>1.0)]
print('WROTE',OUT)
print('N',len(res),'HITS',len(hit))
print((hit if len(hit) else res)[['Strategy','Sharpe','AnnExcessRet','InfoRatio','CAGR','MaxDD']].head(20).to_string(index=False))