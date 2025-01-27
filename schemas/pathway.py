def PathwayEntity(pathway) -> dict:
    return {
        "_id": pathway.get("_id"),
        "title": pathway.get("title"),
        "description": pathway.get("description"),
        "approved": bool(pathway.get("approved")),
        "status": pathway.get("status"),
        "sendEmail": bool(pathway.get("sendEmail")),
    }
