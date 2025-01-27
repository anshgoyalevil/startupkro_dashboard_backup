from fastapi import APIRouter

status = APIRouter()


@status.get("/status")
async def get_status():
    return {"status": "ok"}
