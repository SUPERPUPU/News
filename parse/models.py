from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    #num = models.IntegerField(max_length=20)
    #photo = models.URLField(blank=True)
    #created_at = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.name