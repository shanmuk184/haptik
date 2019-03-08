from dynamic_rest import serializers
from dynamic_rest.fields import DynamicMethodField, DynamicRelationField
from django.contrib.auth.models import User
from feed.models import TweetModel, FollowModel

class UserSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model=User
        fields=("username",)

class TweetSerializer(serializers.DynamicModelSerializer):
    user = UserSerializer()
    class Meta:
        model = TweetModel
        fields=("text", "user", "created_at")

class UserProfileSerializer(serializers.DynamicModelSerializer):
    tweets =TweetSerializer(many=True,read_only=True)
    class Meta:
        model = User
        fields = ("tweets",) 

class FollowSerializer(serializers.DynamicModelSerializer):
    target = DynamicMethodField(requires=["target"])
    
    def get_target(self, instance):
        target = instance.target
        tweets = UserProfileSerializer(target).data 
        if tweets["tweets"]:
            return tweets  

    class Meta:
        model = FollowModel
        fields = ("target",)


class FeedSerializer(serializers.DynamicModelSerializer):
    feed = DynamicMethodField()
    def get_feed(self, instance):
        follows = instance.follows.all()
        data = []
        for follow in follows:
            following_userdata = FollowSerializer(follow).data
            if following_userdata["target"]:
                for tweet in following_userdata["target"]["tweets"]:
                    data.append(tweet)
        return sorted(data, key=lambda x:x["created_at"], reverse=True)

    class Meta:
        model = User
        fields = ("feed",)