# Tenant Visibility Bug

High-level bug: `visible_projects` returns every project for a user and ignores the user's organization. A user must only see projects belonging to their own organization.

Run the reproduction with:

```powershell
python repro.py
```

Run the failing test with:

```powershell
python -m pytest -q
```

Expected result: an `acme` user sees only `acme-api`, but the buggy implementation also exposes `globex-billing`.
