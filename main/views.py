from django.http import HttpResponse
from django.shortcuts import render

from .models import Tweets
from request_x import request_tweet


def get_tweet_info():
    ids = []

    res, id_list = request_tweet()

    qs = Tweets.objects.filter(tweet_id__in=id_list).values_list('tweet_id', flat=True)

    create_list = []
    for i in res:
        if i.get("id") in qs:
            continue
        create_list.append(
            Tweets(
                tweet_id=i.get("id"),
                content=i.get("content"),
                create_time=i.get("create_time"),
            )
        )
    print("准备放到数据库的内容", create_list)
    Tweets.objects.bulk_create(create_list)


def x(request):
    get_tweet_info()
    return HttpResponse()


