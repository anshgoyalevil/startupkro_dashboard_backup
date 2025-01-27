def NoteEntity(note) -> dict:
    return {
        "_id": note.get("_id"),
        "information": note.get("information"),
        "private": bool(note.get("private")),
        "approved": bool(note.get("approved")),
        "createdAt": note.get("createdAt"),
    }


def NoteEntityList(notes) -> list:
    return [NoteEntity(note) for note in notes]
