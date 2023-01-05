from django.shortcuts import render
from .models import Notifications
from django.views.generic import CreateView,ListView
from django.urls import reverse_lazy
from .forms import PostForm
# Create your views here.
class CreatePostView(CreateView):
    model = Notifications
    form_class = PostForm
    template_name = 'notifications/notifications.html'
    success_url = reverse_lazy('home')

class HomePageView(ListView):
    model = Notifications
    template_name = 'notifications/redirect.html'