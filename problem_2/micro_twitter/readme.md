### Documentation in Micro Twitter

## Login and Signup
```
    # I used django default authentication to create views for Login and SignUp
    # You have to go to localhost:8000/signup to create your account
    # For signin you have to go to localhost:8000/accounts/login to login to your account
```
## Tweet and Follow
```
    # I created a view called Tweet in views.py, micro_twitter that saves response
    # in Tweet table.
    # I craeted a view called Follow in views.py, micro_twitter that makes the first user follow target user.
```
## Feed
```
    # I created a view called FeedView in feed app that displays user feed. Feed includes tweets added by # the users followed by logged in user
```
## Data Format for feed
```
    # Data iam sending is an array of objects
    # Each object structure is :
    {
        "user":<username>,
        "text":<tweet>,
        "created_at":<created_at>
    } 
    # items are sorted using created_at value and returns to user 
```

## Data Model
```
    # There are two custom models i am using in this app  
    # They are FollowModel, TweetModel.
    # FollowModel stores manytomany relationship for user followers We can get 
    # User following using "follows" related manager.
    # Tweet model stores foreignKey to user model and tweet text.   
```

## Serializers
```
    # I used dynamic_rest serializers to return json data.
    # You can check them in serializers.py
    # Main serializer that connects all others is FeedSerializer 
```