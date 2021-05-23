from django.urls import path
from .views import index
from .import short_view

urlpatterns = {
    path('', index),
    path('s/', short_view.short_url)
}