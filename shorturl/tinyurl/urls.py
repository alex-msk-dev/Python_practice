from django.urls import path
from .views import index
from .import short_view
from .import long_view

urlpatterns = {
    path('', index),
    path('s/', short_view.short_url),
    path('s/<str:key>', long_view.full_url)
}