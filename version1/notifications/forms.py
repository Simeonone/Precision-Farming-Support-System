from django import forms
from .models import Notifications
class PostForm(forms.ModelForm):

    class Meta:
        model = Notifications
        fields = ['message', 'image']