from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Thread(models.Model):
    title = models.CharField(max_length=100, verbose_name="スレッドタイトル")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.title

class Response(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    number = models.IntegerField()
    name = models.CharField(max_length=100, default='名無しさん', verbose_name="名前")
    random_id = models.CharField(max_length=10)
    text = models.TextField(max_length=1000, verbose_name="コメント内容")
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.text