from django.db import models

# Create your models here.
class Alarm(models.Model):
  title = models.CharField(max_length=255)
  time = models.DateTimeField()
  active = models.BooleanField()

  def __str__(self):
    return self.title

