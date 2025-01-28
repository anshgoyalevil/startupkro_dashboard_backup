def ChatboxEntity(chatbox) -> dict:
    return {
        "_id": str(chatbox.get("_id")),
        "serviceName": chatbox.get("serviceName"),
        "assignedFor": chatbox.get("assignedFor"),
        "serviceId": str(chatbox.get("serviceId")),
        "participants": [str(id) for id in chatbox.get("participants", [])],
        "messages": [{"_id": str(message.get("_id")), "content": message.get("content"), "senderName": message.get("senderName"), "timestamp": message.get("timestamp")} for message in chatbox.get("messages", [])],
    }


def ChatboxEntityList(chatboxes) -> list:
    return [ChatboxEntity(chatbox) for chatbox in chatboxes]
