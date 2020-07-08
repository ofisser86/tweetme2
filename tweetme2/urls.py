"""tweetme2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from tweets.views import (
    home_view,
    tweet_detail_view,
    tweets_list_view,
    tweet_create_view,
    tweet_delete_view,
    tweet_action_view
                        )


urlpatterns = [
    path('', home_view, name='home'),
    path('react', TemplateView.as_view(template_name='react.html')),
    path('tweets', tweets_list_view, name='tweets_list'),
    path('create-tweet', tweet_create_view, name='create-tweet'),
    path('tweet/<int:tweet_id>', tweet_detail_view, name='tweet_detail'),
    # path('api/tweet/action', tweet_action_view, name='tweet_action'),
    # path('api/tweet/<int:tweet_id>/delete', tweet_delete_view, name='tweet_delete'),
    path('api/tweets/', include('tweets.urls')),


    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)