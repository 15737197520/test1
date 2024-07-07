from django.contrib import admin
from .models import Tweets, RequestUsers


@admin.register(Tweets)
class TweetAdmin(admin.ModelAdmin):
    list_display = ['tweet_id', 'content']


@admin.register(RequestUsers)
class RequestUsersAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'description']

