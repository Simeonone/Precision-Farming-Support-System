from django.urls import path
from .views import CreatePostView, HomePageView

urlpatterns = [
    path('', CreatePostView.as_view(), name='add_post_2'), # new
    path('redirect/', HomePageView.as_view(), name='home') # new
]