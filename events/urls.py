from django.urls import path
from .views import (
    HomeView, EventListView, EventDetailView, 
    OrganizerEventListView, EventCreateView, EventUpdateView, 
    EventDeleteView, SessionCreateView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('events/', EventListView.as_view(), name='event_list'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('organizer/events/', OrganizerEventListView.as_view(), name='organizer_events'),
    path('organizer/events/create/', EventCreateView.as_view(), name='event_create'),
    path('organizer/events/<int:pk>/edit/', EventUpdateView.as_view(), name='event_update'),
    path('organizer/events/<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),
    path('organizer/events/<int:event_id>/sessions/create/', SessionCreateView.as_view(), name='session_create'),
]

