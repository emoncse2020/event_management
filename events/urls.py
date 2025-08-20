from django.urls import path
from .views import create_event, organizer_dashboard, update_event, delete_event

urlpatterns = [
    path('create-event/', create_event, name='create-event'),
    path('event/<int:id>/update/',update_event, name='update-event' ),
    path('event/<int:id>/delete/', delete_event, name='delete-event'),
    path('organizer-dashboard/', organizer_dashboard, name='organizer-dashboard'),
  
    
]
