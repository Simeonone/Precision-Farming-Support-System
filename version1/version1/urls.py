"""version1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as users_views
from convert import views as convert_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from cropimage.views import main_view
from notifications import views as notifications_views
#line/code statement above takes care of user login and logout
#side note- since we are importing multiple views, it's important to use 'as' keyword
#in order to differenciate them
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', users_views.register, name='register'),
    #below 2 lines as per in notebook
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'), #login view.
    #path('login/', auth_views.LoginView.as_view(template_name='users/login.html',redirect_authenticated_user=True), name='login'),
    # its a built in views. it handes everything except the templates
    #as_view(template_name='users/login.html'), name='login') - tells django where to look for the template
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    #code below tells django which code will go to blogs.url
    path('', include('blog.urls')), #blog.urls=blog/urls
    path('profile/', users_views.profile, name='profile'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),

    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),


    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),



    path('getstarted/', users_views.getstarted, name='getstarted'),

    path('cropimage/', main_view, name="main-view"),
 #   path('notifications/',notifications_views.notifications, name='notifications'),
    path('notifications/', include('notifications.urls')),
    path('convert/', convert_views.convert, name='convert'),
    #path('convert2/', convert_views.convert2, name='convert2'),
    path('customerpdf/', include('customerpdf.urls', namespace='customerpdf')),
    path('store/', include('store.urls')),
]

#below checks the debug settings for the code. it's not compulsory tho
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

