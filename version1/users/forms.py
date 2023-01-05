#we can use this form in our view(views.py-it will be inherited there)
# instead of using the UserCreationForm
#we are creating our first form that inherits from the UserCreationForm
#first we import forms as follows:
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

#not that class is same as form
class UserRegisterForm(UserCreationForm): #UserRegistrationForm is a class, or a form that
# inherits from usercreationform
    email = forms.EmailField()
    #if you wish to add firstname, use convention as above, and add the variable to the fields[]...
    #if email is not necessarily requires, type 'email = forms.EmailField(required=False)'
    #default is required=true

    class Meta: #META -> gives us a nested namespace for configurations and keeps the configurations
        #in one place. and within the configuration, we are saying that the model that will be affected
        #is the user model. for example if we do a form.save(), it is going to save to the user model
        model = User #the model that the form interacts with. Its user
        #because whenever the form validates, its going to create a new user
        fields = ['username','email','password1','password2']#these are the fields that
        # are going to be shown on our form. the form shows the specific order in which they
        #appear. password2 = confirm password1


class UserUpdateForm(forms.ModelForm):
    #model form allows us to create a form that will work with a specific database model
    #in this case, i want a model that will update the user model
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']
        #the profile picture isn't here because it will be in my profile model,
        #not user model


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile #the model that we want to work with is profile
        fields = ['image']
         #above - ie 'fields' the fields that we are going to work with

#SIDENOTE- USERUPDATEFORM AND PROFILEUPDATEFORM, when put in the template, will
#look like just one form
#these forms need to be added to the profile view upon creation i.e users>views.py