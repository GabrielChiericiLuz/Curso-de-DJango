from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  
    path('topics/', views.topics, name='topics'),  
    path('topics/<int:topic_id>/', views.topic_entries, name='topic_entries'), 
    path('new_topic/', views.new_topic, name='new_topic'),  # Adicionando a barra no final
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<entry_id>', views.edit_entry, name='edit_entry'),
]
