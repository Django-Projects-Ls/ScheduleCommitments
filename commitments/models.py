from django.db import models

# Create your models here.
class Commitment(models.Model):
  title = models.CharField(max_length=50)
  description = models.TextField()
  date = models.DateTimeField()
  location = models.CharField(max_length=50)

  def __str__(self):
    return f'{self.title} Informações'