from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
#for LISTVIEW: since our homepage is listing all the blog posts
#for DEATILVIEW ABOVE:View for individual posts
from .models import Post
#line above: a query that passes in data from 'posts' class in models.py


def home(request):
    #below is a dictionary called context
    context = {
        #below we query data from database as similarly to in the database shell
        'posts' : Post.objects.all()
        #CFO: when you update the above code, check the HTML i.e. home.html to see if it matches
        #the models.py format
        #spelling mistake!!! you wrote Posts.objects.all()
        #instead of Post.objects.all()
    }
    #return HttpResponse('<h1> Blog Home </h1>')
    return render(request, 'blog/home.html', context)

class PostListView(ListView): #we are importing from listview
    model = Post #creates a list view
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html - the generic class based view is going
    #to be looking for a template with the naming convention: <app>/<model>_<viewtype>.html .
    # ie app = app name(blog) and then a template with the model name which is going to be
    # post then an underscore, then the view type(detail) : ie blog/post_detail.html. generic means condensed
    #lines of code like in Postdetailview
    #HERE,  a template was created with the name 'deatil.html so the browser can find it automatically
    #without needing to specify a template name like i did in the post list view
    context_object_name = 'posts'
    #below changes the order my query is making to the database
    #the following code sets the posts from oldest to newest: ordering = ['date_posted']
    #if you want it to go from newest to oldest, do as below:
    ordering = ['-date_posted']
    #the code below shows how many posts per page there should be
    paginate_by = 5
    
    

class UserPostListView(ListView): #we are importing from listview
    model = Post #creates a list view
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
#this is a view with a form where i create a new form
#this is a view with a form where i create a new form
#so the only other thing needed are the fields that i want to be in that form
#e.g. title and content. date posted will be filled in automatically
    model = Post
    fields = ['title','content']
#here we need to override the form valid method. this is because if you dont, it will bring an integrity
#error because the system doesnt know if the currently logged in user should be associated with an updated
#post. a method called form_valid was created as shown below:
    def form_valid(self, form):
        #we set the author on the form as below:
        form.instance.author = self.request.user
        #above: author = currently logged in user
        return super().form_valid(form)

#IMPORTANT: mixins must be to the left of the updateview
class PostUpdateView (LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    #we need to require the user is logged in - LoginRequiredMixin
    #we also need a certain user to be the author of a post- UserPassesTestMixin
    model= Post
    fields = ['title','content']
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    #the post below prevents unauthorized users from editing other users' posts
    def test_func(self):
        post = self.get_object() #this one gets the post we are currently trying to update
        #this one tries to get if the current post belongs to the currently active user
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    #code below: success url upon deletion
    success_url = '/'
    def test_func(self):
        post = self.get_object() #this one gets the post we are currently trying to update
        #this one tries to get if the current post belongs to the currently active user
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title':'about'})