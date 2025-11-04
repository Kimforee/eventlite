# EventLite (Models-Only Starter)

This is the **models-only** starter for the EventLite take-home assignment.

Included:
- Django project scaffolding
- Apps: `accounts`, `events`
- **Models defined** for Profile, Event, Session, Bookmark, Comment, Notification

Excluded (candidate must implement):
- Views (all CBVs)
- URLs
- Templates
- Static assets
- Context processor, custom decorator, pagination, jQuery interactions

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```