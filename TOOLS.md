# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Python

- Reusable virtual environment: `/home/msands/.openclaw/workspace/claw-venv`
- Activate: `source /home/msands/.openclaw/workspace/claw-venv/bin/activate`
- Core packages preinstalled: `psycopg[binary]`, `pandas`, `sqlalchemy`

## PostgreSQL

- Host: `<REDACTED_HOST>`
- Port: `5432`
- Database: `marketlab`
- Username: `<REDACTED_USER>`
- Password: `<REDACTED_USER>`
- Access: read-only across all schemas/tables (as granted by Michael)
- Connection URI: `postgresql://<REDACTED_USER>:<REDACTED_PASS>@<REDACTED_HOST>:5432/marketlab`

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.
