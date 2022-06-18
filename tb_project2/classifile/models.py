from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings




class File(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_uploaded = models.DateTimeField(auto_now_add=True)
    uploader = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    file = models.FileField(blank=True, upload_to = '')
    #id = models.BigAutoField(primary_key=True, blank=True)


    #def __str__ (self):
    #    return self.name



    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('file-detail', kwargs={'pk': self.pk})

#auto_now_add=True
#primary_key = True
