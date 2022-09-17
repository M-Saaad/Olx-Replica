from django.conf.urls import url
from AdminApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^userlogin$', views.userLoginApi),
    url(r'^userlogin/([0-9]+)$', views.userLoginApi),

    url(r'^usersignup$', views.userSignupApi),
    url(r'^usersignup/([0-9]+)$', views.userSignupApi),

    url(r'^laptop$', views.laptopApi),
    url(r'^laptop/([0-9]+)$', views.laptopApi),

    url(r'^mobile$', views.mobileApi),
    url(r'^mobile/([0-9]+)$', views.mobileApi),

    url(r'^userdetails$', views.userDetailApi),
    url(r'^userdetails/([0-9]+)$', views.userDetailApi),

    url(r'^savefile', views.SaveFile),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)