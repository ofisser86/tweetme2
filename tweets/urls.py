from django.contrib import admin
from django.urls import path

from .views import (
    home_view,
    tweet_detail_view,
    tweets_list_view,
    tweet_create_view,
    tweet_delete_view,
    tweet_action_view
                        )

'''
Endpoint for the urls api/tweets/xxx
'''

urlpatterns = [
    path('', tweets_list_view, name='tweets_list'),
    path('create/', tweet_create_view, name='create-tweet'),
    path('action/', tweet_action_view, name='tweet_action'),
    path('<int:tweet_id>/', tweet_detail_view, name='tweet_detail'),
    path('<int:tweet_id>/delete/', tweet_delete_view, name='tweet_delete'),
]
