from django.urls import path

from . import views

# the name detail might be a little bit confusing, therefore implement app_name
app_name = 'item'

urlpatterns = [
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
]