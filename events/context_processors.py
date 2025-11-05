from .models import Notification, Bookmark

def global_counts(request):
    """Context processor to provide global counts in navbar"""
    context = {}
    
    if request.user.is_authenticated:
        # Unread notifications count
        context['unread_notifications_count'] = Notification.objects.filter(
            user=request.user, 
            is_read=False
        ).count()
        
        # Bookmarks count
        if hasattr(request.user, 'profile') and request.user.profile.role == 'ATTENDEE':
            context['my_bookmarks_count'] = Bookmark.objects.filter(user=request.user).count()
        else:
            context['my_bookmarks_count'] = 0
    else:
        context['unread_notifications_count'] = 0
        context['my_bookmarks_count'] = 0
    
    return context

