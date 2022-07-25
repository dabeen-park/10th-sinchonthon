"""sinchonthon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
# from django.urls.conf import include
from django.contrib import admin
from django.urls import path, include
import user.views
import sinchonsite.views

from mypage import views as mypage_views
urlpatterns = [
    path('admin/', admin.site.urls),
    
    # social login
    path('user/login', user.views.login_view, name='login'),
    path('user/logout', user.views.logout_view, name='logout'),
    path('user/signup', user.views.signup_view, name='signup'),
    # path('user/', include('user.urls')),
    path('user/', include('allauth.urls')),
    path('mypage/', mypage_views.mypage, name='mypage'),
    path('mypage2/' , mypage_views.mypage2, name='mypage2'),
    path('mypage3/' , mypage_views.mypage3, name='mypage3'),

    path('sinchong/' , mypage_views.sinchong, name='sinchong'),
    path('sinchong2/' , mypage_views.sinchong2, name='sinchong2'),

]
