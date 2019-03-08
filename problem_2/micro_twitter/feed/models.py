from django.db import models

# Create your models here.
class TweetModel(models.Model):
    id = models.AutoField(primary_key=True,)
    user = models.ForeignKey("auth.User", related_name="tweets",on_delete=models.CASCADE)
    text = models.CharField(max_length=140,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "feed_tweet"


class FollowModel(models.Model):
    user = models.ForeignKey("auth.User", related_name="follows", on_delete=models.CASCADE,null=True, blank=True)
    target = models.ForeignKey("auth.User", related_name="followers", on_delete=models.CASCADE,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'target')
        db_table = "feed_follow"

# class FeedModel(models.Model):
#     user = models.ForeignKey("auth.User", related_name="feed", on_delete=models.CASCADE)
