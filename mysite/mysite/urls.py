from django.contrib import admin
from django.urls import path, include


# Admin urls
urlpatterns = [
    path('admin/', admin.site.urls),
]

# App's include
urlpatterns += [
    path('polls/', include('polls.urls')),
]

