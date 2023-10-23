from django import forms
from .models import Commitment

class CommitmentsForms(forms.ModelForm):
    class Meta:
        model = Commitment
        fields = ('nome', 'data', 'descricao', 'local', 'dress_code')
