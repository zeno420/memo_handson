from django.db import models

class Memo(models.Model):
    title = models.CharField(max_length=200)
    text  = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class Attachment(models.Model):
    memo = models.ForeignKey(Memo, on_delete=models.CASCADE)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
