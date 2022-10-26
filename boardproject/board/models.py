from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Thread(models.Model):
    title = models.CharField(max_length=100, verbose_name="スレッドタイトル")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delete_code = models.CharField(max_length=10, null=True, blank=True, verbose_name="削除用コード")

    def __str__(self):
        return self.title

class Response(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    number = models.IntegerField()
    name = models.CharField(max_length=100, default='名無しさん', verbose_name="名前")
    email = models.EmailField(max_length=254, verbose_name="メールアドレス", null=True, blank=True)
    text = models.TextField(max_length=1000, verbose_name="コメント内容")
    random_id = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delete_code = models.CharField(max_length=10, null=True, blank=True, verbose_name="削除用コード")

    def __str__(self):
        return self.text

class Key(models.Model):
    key = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.key