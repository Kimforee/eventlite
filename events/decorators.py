from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

def organizer_required(view_func):
    """Decorator to check if user is an organizer"""
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if not hasattr(request.user, 'profile') or request.user.profile.role != 'ORGANIZER':
            raise PermissionDenied("Only organizers can access this page.")
        return view_func(request, *args, **kwargs)
    return wrapper

