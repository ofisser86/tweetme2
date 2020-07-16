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
from django.urls import path, re_path, include  # url()
from django.views.generic import TemplateView

from accounts.views import (
    login_view,
    logout_view,
    register_view,
)

from tweets.views import (
    tweets_list_view,
    tweets_detail_view,
    tweets_detail_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tweets_list_view),
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
    path('<int:tweet_id>', tweets_detail_view),
    re_path(r'profiles?/', include('profiles.urls')),
    path('api/tweets/', include('tweets.api.urls'))

    # path('', home_view, name='home'),

    # path('react', TemplateView.as_view(template_name='react.html')),

    # path('tweets', tweets_list_view, name='tweets_list'),
    # path('create-tweet', tweet_create_view, name='create-tweet'),
    # path('tweet/<int:tweet_id>', tweet_detail_view, name='tweet_detail'),
    # path('api/tweet/action', tweet_action_view, name='tweet_action'),
    # path('api/tweet/<int:tweet_id>/delete', tweet_delete_view, name='tweet_delete'),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
