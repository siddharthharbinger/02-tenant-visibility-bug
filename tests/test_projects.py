from projects import visible_projects


def test_projects_are_isolated_by_organization():
    assert [project["id"] for project in visible_projects("acme")] == ["acme-api"]
