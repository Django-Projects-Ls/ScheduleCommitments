from django.db import models

# Create your models here.
class Commitment(models.Model):
    nome = models.CharField(max_length=255)
    data = models.DateField()
    descricao = models.TextField()
    local = models.CharField(max_length=255)
    dress_code = models.TextField()
    
    def __str__(self):
        return f"{self.nome}'s Information"