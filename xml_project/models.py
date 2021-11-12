from django.db import models


class FileXML(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default='')
    title = models.CharField(max_length=64)
    content = models.TextField()

    def __str__(self):
        return self.title