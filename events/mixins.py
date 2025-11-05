from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin

class OrganizerRequiredMixin(LoginRequiredMixin):
    """Mixin to check if user is an organizer - for Class-Based Views"""
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if not hasattr(request.user, 'profile') or request.user.profile.role != 'ORGANIZER':
            raise PermissionDenied("Only organizers can access this page.")
        return super().dispatch(request, *args, **kwargs)

