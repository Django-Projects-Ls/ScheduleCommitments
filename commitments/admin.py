from django.contrib import admin
from .models import Commitment

# Register your models here.
class CommitmentFields(admin.ModelAdmin):
  list_display = ['nome', 'data', 'local']

admin.site.register(Commitment, CommitmentFields)