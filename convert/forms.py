from django.forms import ModelForm
from .models import Upload

class UploadImageForm(ModelForm):
    class Meta:
        model = Upload
        fields = ['image']