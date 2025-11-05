from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    # Intentionally left empty — candidate must wire URLs.
    path('admin/', admin.site.urls),
    path('', include('events.urls')),
    path('accounts/', include('accounts.urls')),
]
