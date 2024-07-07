from django.db import models


class Tweets(models.Model):
    # username = models.CharField(verbose_name=)
    tweet_id = models.CharField(verbose_name="tweetid", max_length=255, db_index=True)
    content = models.TextField(verbose_name="tweet内容")
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "推特信息"
        verbose_name_plural = verbose_name


class RequestUsers(models.Model):
    user_id = models.CharField(verbose_name="用户id", max_length=255)
    description = models.CharField(verbose_name="用户描述", max_length=255, null=True, blank=True)

    def __str__(self):
        return self.description or self.user_id

    class Meta:
        verbose_name = "爬取用户"
        verbose_name_plural = verbose_name

