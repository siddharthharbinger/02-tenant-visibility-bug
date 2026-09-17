from projects import visible_projects


actual = [project["id"] for project in visible_projects("acme")]
expected = ["acme-api"]
print(f"actual={actual} expected={expected}")
raise SystemExit(0 if actual == expected else 1)
