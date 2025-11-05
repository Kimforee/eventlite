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

## Reasoning Questions

### 1. ORM Optimization

The Event list and detail views use:

```python
Event.objects.select_related('organizer').prefetch_related('sessions', 'bookmarks', 'comments__author')

```

`select_related` reduces queries for foreign key fields like organizer, while `prefetch_related` efficiently fetches related sets such as sessions and comments. This eliminates the N+1 query problem and improves performance.

### 2. Context Processor

A custom context processor provides globally available data to templates:

```python
def global_counts(request):
    if request.user.is_authenticated:
        return {
            "unread_notifications_count": Notification.objects.filter(recipient=request.user, is_read=False).count(),
            "my_bookmarks_count": Bookmark.objects.filter(user=request.user).count(),
        }
    return {}

```

This allows consistent display of notification and bookmark counts in the navbar without repeating logic in each view.

### 3. Custom Decorator

The `@organizer_required` decorator ensures that only organizers can access event management views:

```python
def organizer_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("events:login")
        if not hasattr(request.user, "profile") or request.user.profile.role != "organizer":
            return HttpResponseForbidden("403 – Organizer access only")
        return view_func(request, *args, **kwargs)
    return wrapper

```

This enforces role-based permissions and cleanly separates access control from business logic.

## Project Structure

```
eventlite/
├── eventlite/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── events/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── templates/events/
│   └── static/core/
├── manage.py
└── README.md

```

## Technologies Used

-   Django 5.x
-   SQLite (default database)
-   HTML, CSS, jQuery
-   Django Templates
    

## Anti-AI Pledge

“I confirm that no code or text in this submission was produced by any AI tool (e.g., ChatGPT, Copilot).  
Any automated generation (e.g., icons or placeholder text) used is explicitly listed with its exact prompt.”

Note: During development, I used **Cursor** only for **UI-related code autocompletions and formatting assistance**.  
All core logic, models, and views were written manually/auto-completion.


## Checklist
-   Functional Django app running with `python manage.py runserver`
-   Authentication and user roles implemented
-   Event and session CRUD using CBVs
-   ORM optimization with `select_related` and `prefetch_related`
-   Custom decorator and context processor implemented
-   AJAX interactions for bookmarks and comments
-   Pagination and clean UI
-   Code adheres to Django conventions and best practices