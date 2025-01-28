from schemas.pathway import PathwayEntity


def TemplateEntity(template) -> dict:
    return {
        "_id": str(template.get("_id")),
        "templateName": template.get("templateName"),
        "pathway": [PathwayEntity(pathway) for pathway in template.get("pathway", [])]
    }


def TemplateEntityList(templates) -> list:
    return [TemplateEntity(template) for template in templates]
