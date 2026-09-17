PROJECTS = [
    {"id": "acme-api", "org_id": "acme", "name": "Acme API"},
    {"id": "globex-billing", "org_id": "globex", "name": "Globex Billing"},
]


def visible_projects(user_org_id: str) -> list[dict[str, str]]:
    """Return projects visible to the current organization."""
    return list(PROJECTS)
