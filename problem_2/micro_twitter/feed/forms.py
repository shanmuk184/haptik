from django import forms

from .models import TweetModel, FollowModel

class TweetForm(forms.ModelForm):

    class Meta:
        model = TweetModel
        fields = ( 'user','text',)


class Follow(forms.ModelForm):
    class Meta:
        model = FollowModel
        fields = ('user', 'target',)
        