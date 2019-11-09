from django.db import models

# Create your models here.

class Website(models.Model):
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Tag(models.Model):
    website = models.ForeignKey(Website,on_delete=models.CASCADE)
    keyword = models.CharField(max_length=20)
    value = models.IntegerField(default=0)

    def __str__(self):
        return self.keyword