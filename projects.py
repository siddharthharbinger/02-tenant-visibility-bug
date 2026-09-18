PROJECTS = [
    {"id": "acme-api", "org_id": "acme", "name": "Acme API"},
    {"id": "globex-billing", "org_id": "globex", "name": "Globex Billing"},
]
def visible_projects(user_org_id: str) -> list[dict[str, str]]:
    """Return projects visible to the specified organization."""
    # Only include projects whose org_id matches the provided user_org_id.
    return [project for project in PROJECTS if project["org_id"] == user_org_id]
    """Return projects visible to the current organization."""
    return list(PROJECTS)
