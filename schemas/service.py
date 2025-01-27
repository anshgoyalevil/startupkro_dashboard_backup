from schemas.pathway import PathwayEntity
from schemas.note import NoteEntityList


def ServiceEntity(service) -> dict:
    return {
        "_id": str(service.get("_id")),
        "timelineDatesIsVisible": service.get("timelineDatesIsVisible"),
        "name": service.get("name"),
        "cost": service.get("cost"),
        "status": service.get("status"),
        "pathway": [PathwayEntity(pathway) for pathway in service.get("pathway")],
        "duration": service.get("duration"),
        "assignedFor": {
            "username": service.get("assignedFor").get("username"),
            "userId": str(service.get("assignedFor").get("userId")),
            "email": service.get("assignedFor").get("email"),
        },
        "assignedTo": {
            "username": service.get("assignedTo").get("username"),
            "userId": str(service.get("assignedTo").get("userId")),
            "email": service.get("assignedTo").get("email"),
        },
        "notes": NoteEntityList(service.get("notes", [])),
    }


def ServiceEntityList(services) -> list:
    return [ServiceEntity(service) for service in services]
