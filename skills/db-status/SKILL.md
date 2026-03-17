---
name: db-status
description: Generate the daily database status report for MarketLab batch jobs and post to Slack.
---

The output should be in the following format:
***
[Jobs]:
Name: 01_constituents.py    | Last Run: 2024-06-01 00:00    | Max Date: 2024-06-02 00:00    | Status: Updated
...[repeat for each respective script]...

[Messages]:
Provide any relevant notes, messages or errors in this section as markdown text. For example, if a script has not been updated, provide the error message or reason for the failure here. 
***

Where:
  Name = The name of the python script that is run from database/batch/
  Last Run = Timestamp of the last time the script was executed
  Max Date = The maximum date for which the script has successfully populated data in the database. Determine based on a select(max(date)) query to the relevant table.
  Status = Updated if Max Date is euqal to either the previous or current business date. Stale if it is not.
  Emoji = An emoji representing the job status of updated (green check) or stale (red X)

The Jobs section should contain only the data in the format specified above. Do not add any additional text to that section. You may add text to the Messages section.

Formatting requirements (strict):
- Wrap the entire output in one fenced markdown code block using triple backticks so Slack renders monospaced text.
- In the [Jobs] section, preserve spacing exactly and keep columns visually aligned.
- Keep the same indentation/whitespace pattern across all job lines.
- Use this exact line template for every job (including internal spacing):
  `Name: <job_name><spaces>| Last Run: <timestamp><spaces>| Max Date: <timestamp><spaces>| Status: <Updated|Stale> | Emoji: <>>`
- Ensure every `|` delimiter is vertically aligned across all job lines. (Very Important!!)
- Use fixed-width style padding so each line has aligned columns in this order:
  Name | Last Run | Max Date | Status | Emoji

Execution requirements:
- Run implementation with this interpreter so required DB packages are available:
  `/home/msands/.openclaw/workspace/claw-venv/bin/python`
- Use `psycopg` from that environment for database queries.
- Never return raw traceback/exec errors to Slack.

Send the output to me as a Slack message in markdown format.
