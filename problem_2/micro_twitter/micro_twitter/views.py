from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from feed.forms import TweetForm, Follow
from rest_framework.response import Response
from django.shortcuts import redirect
from feed.serializers import TweetSerializer
from django.http.response import HttpResponseRedirect

from feed.models import TweetModel
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('feed')
    template_name = 'signup.html'

class Tweet(generic.CreateView):
    #model = TweetModel
    form_class = TweetForm
    template_name = 'tweet.html'
    success_url = reverse_lazy('feed')
    def post(self, request, **kwargs):
        user = request.user
        text = request.POST["tweet"]
        form =self.form_class(data={"user":user.id, "text":text})
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/feed/")
        else:
            raise KeyError

class Follow(generic.CreateView):
    form_class = Follow
    template_name = 'follow.html'
    success_url = reverse_lazy('feed')
    


