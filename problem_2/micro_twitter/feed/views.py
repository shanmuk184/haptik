from django.shortcuts import render
from rest_framework.views import APIView
from dynamic_rest import viewsets
from feed.serializers import FollowSerializer, FeedSerializer, TweetSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer


#Create your views here.
class TweetView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'tweet.html'
    serializer = TweetSerializer

    def post(self, request):
        user = User.objects.get(id=request.user.id)
        text = request.data["text"]
        serializer = self.get_serializer()
        tweet = serializer(data={"user":user, "text":text})
        if tweet.is_valid():
            tweet.save()
            return Response()

class FollowView(APIView):
    def post(self, request):
        user = User.objects.get(pk=request.data["user"])
        follows = User.objects.get(pk=request.data["follows"])
        serializer = FollowSerializer(data={"user":user, "target":follows})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


class FeedView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'feed.html'


    def get(self, request, format=None):
        user = User.objects.get(id=request.user.pk)
        
        serializer = FeedSerializer(user)

        return Response({"data":serializer.data})
