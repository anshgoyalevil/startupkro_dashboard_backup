from fastapi import FastAPI

# Routes
from routes.status import status
from routes.backup import backup

app = FastAPI()
app.include_router(status)
app.include_router(backup)
