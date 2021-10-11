from django.db import models

# Create your models here.
class createnotes(models.Model):
    title=models.CharField(max_length=150)
    text=models.TextField(blank=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True,verbose_name="updated date")
    image=models.ImageField(blank=True)
    user_id=models.TextField(blank=True)

    def __str__(self):
        return f"{self.id} - {self.title}"

    