from django.contrib import admin
from .models import Tweets


@admin.register(Tweets)
class TweetAdmin(admin.ModelAdmin):
    list_display = ['tweet_id', 'content']
