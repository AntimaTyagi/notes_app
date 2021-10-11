from django.db import models
from datetime import datetime
import os # new
from pathlib import Path

def get_file_path(instance,filename):
    now = datetime.now()
    #/media/images/2021/09/28/hell.png
    return os.path.join("images",f"{now.year}/{now.month}/{now.day}/",filename)

# Create your models here.
class createnotes(models.Model):
    title=models.CharField(max_length=150)
    text=models.TextField(blank=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True,verbose_name="updated date")
    image=models.ImageField(upload_to=get_file_path ,blank=True)
    user_id=models.TextField(blank=True)

    def __str__(self):
        return f"{self.id} - {self.title}"

    