from django.shortcuts import render
from .forms import UploadImageForm
# Create your views here.

def convert(request):
    form = UploadImageForm()
    if request.method == 'POST':
        form = UploadImageForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'convert/convert.html', context)

