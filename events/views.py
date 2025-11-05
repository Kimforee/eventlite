from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Event, Session
from .forms import EventForm, SessionForm
from .mixins import OrganizerRequiredMixin

class HomeView(TemplateView):
    template_name = 'events/home.html'

class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'
    paginate_by = 10
    
    def get_queryset(self):
        # Optimize queries: select_related for foreign keys, prefetch_related for reverse relations
        queryset = Event.objects.select_related('organizer').prefetch_related('sessions', 'bookmarks')
        # Search functionality
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)
        return queryset.order_by('-created_at')

class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'
    
    def get_queryset(self):
        # Optimize queries: avoid N+1 queries by prefetching related objects
        return Event.objects.select_related('organizer').prefetch_related(
            'sessions', 
            'comments__author',
            'bookmarks'
        )

class OrganizerEventListView(OrganizerRequiredMixin, ListView):
    model = Event
    template_name = 'events/organizer_events.html'
    context_object_name = 'events'
    
    def get_queryset(self):
        return Event.objects.filter(organizer=self.request.user).order_by('-created_at')

class EventCreateView(OrganizerRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'
    success_url = reverse_lazy('organizer_events')
    
    def form_valid(self, form):
        form.instance.organizer = self.request.user
        return super().form_valid(form)

class EventUpdateView(OrganizerRequiredMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'
    success_url = reverse_lazy('organizer_events')
    
    def get_queryset(self):
        return Event.objects.filter(organizer=self.request.user)

class EventDeleteView(OrganizerRequiredMixin, DeleteView):
    model = Event
    template_name = 'events/event_confirm_delete.html'
    success_url = reverse_lazy('organizer_events')
    
    def get_queryset(self):
        return Event.objects.filter(organizer=self.request.user)

class SessionCreateView(OrganizerRequiredMixin, CreateView):
    model = Session
    form_class = SessionForm
    template_name = 'events/session_form.html'
    
    def get_event(self):
        return get_object_or_404(Event, pk=self.kwargs['event_id'], organizer=self.request.user)
    
    def form_valid(self, form):
        form.instance.event = self.get_event()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('event_detail', kwargs={'pk': self.kwargs['event_id']})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event'] = self.get_event()
        return context

