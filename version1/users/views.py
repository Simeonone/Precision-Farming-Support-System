from django.shortcuts import render, redirect #redirect helps the user get redirected upon
# successfully creating an account
#from django.contrib.auth.forms import UserCreationForm #-this has been rid of cause were using UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# ABOVE line-requires a user to be logged in before they can access a page. like a session
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
#ABOVE line-from forms.py. here, i replaced (2) UserCreationForm with UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid(): # tells us if form is valid when form is submitted
            form.save() # saves the user info. The password is automatically hash secured
            username = form.cleaned_data.get('username') #the validated form data will be in the
            #form.cleaned_data dictionary, which will be converted to python types from the form
            #flash message to show that we've received valid data- that sends one time alerts to a
            #template that will only be displayed once and disappear on the next request- from
            #the from...import messages
            messages.success(request, f'Account created for {username}. Log In to continue') #after, we redirect
            # the user to another page(home page)
            #f above represents an f string.
            return redirect('login') #login got from template
            ## return redirect('blog-home')
            #blog-home got from blog>urls.py
            #remember to update template to show the flash message.
            #to see hw it was done, go to base.html, find {% block content %}{% endblock %}
            #and see the code above it and below the <!--flash message shown here--> comment
    else:
        form = UserRegisterForm() #if get request, then display a blank form
    #above code: in register.html, we said we want a POST request
    #now we said in the code that when we get a post request then we can validate the data
    #if get request, then display a blank form
    return render(request, 'users/register.html', {'form' : form})


#types of messages:
#messages.debug
#messages.info
#messages.success
#messages.warning
#messages.error

def getstarted(request):
    return render(request, 'users/getstarted.html')


@login_required
def profile(request):
    if request.method == 'POST':
#BELOW- we are passing in the post data into our forms
#instance tells what user and profile you want to update
#request.post sends the post data
#request.files requires additional data coming in with the request ie whatever image
#the user tries to upload
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
#if statement below checks if form is valid
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
        #below tells the user the account was successfully updated ad they are redirected
        #back to the profile page
            messages.success(request, f'Your account has been successfully updated')
            #ABOVE-  after, we redirect
            # the user to another page(home page)
            # f above represents an f string.
            return redirect('profile')  # profile got from template
            ## return redirect('blog-home')
            # blog-home got from blog>urls.py
            # remember to update template to show the flash message.
            # to see hw it was done, go to base.html, find {% block content %}{% endblock %}
            # and see the code above it and below the <!--flash message shown here--> comment
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request,'users/profile.html',context)