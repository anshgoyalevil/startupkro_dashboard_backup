from fastapi import APIRouter
from config.db import mongo_client
from schemas.user import UserEntityList
from schemas.service import ServiceEntityList
from schemas.template import TemplateEntityList
from schemas.chatbox import ChatboxEntityList

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


@backup.get("/templates")
async def get_templates():
    templates = mongo_client.startupkro_db.templates.find()
    return {"templates": TemplateEntityList(templates)}


@backup.get("/chatboxes")
async def get_chatboxes():
    chatboxes = mongo_client.startupkro_db.chatboxes.find()
    return {"chatboxes": ChatboxEntityList(chatboxes)}
