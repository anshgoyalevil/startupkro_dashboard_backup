# StartupKro Dashboard Backup Utility

This utility is used to backup the StartupKro dashboard data. It is a simple Python script that uses `pymongo` to fetch data from `MongoDB` URI and convert it to a JSON file and stores those JSON files to the backup drive.

This script doesn't run continuously and requires an HTTP cron client to trigger the backup at required intervals.

### Dependencies

- `pymongo`: for database connection
- `fastapi[standard]`: for triggering the backup worker remotely
- `uvicorn`: for running the FastAPI server (optional since `fastapi[standard]` includes `uvicorn`)
