"""Defines circuit of URL for learning_logs"""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page with a list of all topics
    path('topics/', views.topics, name='topics'),
    # Page with a detail information on a separate topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page for add a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for add a new entry for separate topic
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for edit an entry
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry')
]