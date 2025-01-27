from fastapi import APIRouter
from config.db import mongo_client
from schemas.user import UserEntityList
from schemas.service import ServiceEntityList

backup = APIRouter()


@backup.get("/backup")
async def start_backup():
    return {"backup": "ok"}


@backup.get("/users")
async def get_users():
    users = mongo_client.startupkro_db.users.find()
    return {"users": UserEntityList(users)}


@backup.get("/services")
async def get_services():
    services = mongo_client.startupkro_db.services.find()
    return {"services": ServiceEntityList(services)}
