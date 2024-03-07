from django.contrib import admin
from django.urls import path
from myapp.views import get_time_stories

urlpatterns = [
    path('admin/', admin.site.urls),
    path('getTimeStories/', get_time_stories, name='get_time_stories'),
]
