import asyncio

from django.http import HttpResponse
import logging
from telegram_api import send

from .models import Tweets, RequestUsers
from request_x import request_tweet
from threading import Timer


def loop_monitor():
    t = Timer(60, get_tweet_info)
    t.start()


def get_tweet_info():
    try:

        ids = RequestUsers.objects.all().values_list('user_id', flat=True)
        logging.info("获取要爬取的id为：%s" % ids)
        for the_id in ids:
            logging.info("准备爬取 %s" % the_id)
            res, id_list = request_tweet(the_id)

            qs = Tweets.objects.filter(tweet_id__in=id_list).values_list('tweet_id', flat=True)

            create_list = []
            # 发送给telegram的东西
            send_list = []
            for i in res:
                if i.get("id") in qs:
                    continue
                send_list.append(i)
                create_list.append(
                    Tweets(
                        tweet_id=i.get("id"),
                        content=i.get("content"),
                        create_time=i.get("create_time"),
                    )
                )
            logging.info("准备放到数据库的内容:\n%s" % create_list)

            # 发送给telegram
            for t in send_list:
                # 发送人

                name = t.get("name")
                content = t.get("content")
                operate = t.get("operate")
                media = t.get("media")
                retweeted = t.get("retweeted")
                send_str = ""
                send_str += name+"  " + operate+":\n"
                send_str += "" + content + "\n"

                media_str = ""
                for m in media:
                    media_str += "\n![](%s)" % m + "\n"

                send_str += "\n" + media_str + "\n"

                # 加转发信息
                if retweeted:
                    send_str += "\t" + retweeted['name'] + "\n"
                    send_str += "\t" + retweeted['content'] + "\n"

                    # 转发的相关媒体资源
                    retweeted_media_str = ""
                    for m in retweeted['content']:
                        retweeted_media_str += "\n![](%s)" % m + "\n"

                    send_str += "\t" + retweeted_media_str + "\n"

                asyncio.run(send(content))

            # 存入数据库
            Tweets.objects.bulk_create(create_list)

    except Exception as e:
        logging.error(e)
        raise e

    finally:
        # 开启下一次定时
        loop_monitor()


def x(request):
    get_tweet_info()
    return HttpResponse()


