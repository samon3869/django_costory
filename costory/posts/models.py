from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50, unique=True)
    content = models.TextField()
    dt_created = models.DateTimeField(verbose_name="Data Created", auto_now_add=True)
    dt_modified = models.DateTimeField(verbose_name="Data Modified", auto_now=True)

    def __str__(self):
        return self.title

