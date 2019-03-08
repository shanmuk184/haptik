"""micro_twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
#from feed.views import FeedView, TweetView, FollowView
from django.conf.urls import url
from django.contrib.auth.views import LoginView
from .views import SignUp
from django.views.generic.base import TemplateView
from feed.views import FeedView, TweetView
from .views import Tweet, Follow
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^signup/', SignUp.as_view(), name="signup"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('tweet/', login_required(Tweet.as_view()), name='tweet'),
    url(r'feed/$', login_required(FeedView.as_view()), name="feed"),
    # url(r"tweet/$", TweetView.as_view()),
    url(r"follow/$", login_required(Follow.as_view()), name="follow"),
]

