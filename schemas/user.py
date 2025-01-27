def UserEntity(user) -> dict:
    return {
        "_id": str(user.get("_id")),
        "username": user.get("username"),
        "email": user.get("email"),
        "password": user.get("password"),
        "phone": user.get("phone"),
        "role": user.get("role"),
        "createdAt": user.get("createdAt"),
        "fullname": user.get("fullname"),
        "pendingServices": [{"_id": str(service["_id"]), "name": service["name"], "serviceId": str(service["serviceId"])} for service in user.get("pendingServices", [])],
        "completedServices": [{"_id": str(service["_id"]), "name": service["name"], "serviceId": str(service["serviceId"])} for service in user.get("completedServices", [])],
        "processServices": [{"_id": str(service["_id"]), "name": service["name"], "serviceId": str(service["serviceId"])} for service in user.get("processServices", [])],
        "onHoldServices": [{"_id": str(service["_id"]), "name": service["name"], "serviceId": str(service["serviceId"])} for service in user.get("onHoldServices", [])],
    }


def UserEntityList(users) -> list:
    return [UserEntity(user) for user in users]
