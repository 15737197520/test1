from django.db import models


class Tweets(models.Model):
    tweet_id = models.CharField(verbose_name="tweetid", max_length=255, db_index=True)
    content = models.TextField(verbose_name="tweet内容")
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "推特信息"
        verbose_name_plural = verbose_name
