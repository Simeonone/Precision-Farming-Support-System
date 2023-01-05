from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views
urlpatterns = [
   ## path('', views.home, name='blog-home'),
    path('', PostListView.as_view(),name='blog-home'),
    #ABOVE CODE has to be converted into an actual view
    #by using as_view
    #homepage cause of the ''
    #views.home is function created in the views.py that returns something
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/', PostDetailView.as_view(),name='post-detail'), #since i am using a class
    #based view, this will be passed to a class based view
    #ABOVE: pk. why pk? because that's what the detail view expects it to be in order to go grab the
    #specific object ie a specific post
    path('post/new/', PostCreateView.as_view(),name='post-create'),
    #a template is needed for the post create view. but its not going to be named as post_create as we named
    #the detail view(post_detail). in real sense, this will share a templae with the updateview that was created
    #ie post_form
    path('post/<int:pk>/update/', PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(),name='post-delete'),
    path('user/<str:username>', UserPostListView.as_view(),name='user-posts'),
]

#<app>/<model>_<viewtype>.html