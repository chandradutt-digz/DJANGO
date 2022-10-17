"""wscubetech URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from wscubetech import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage),
    path('about-us/', views.aboutUs, name='about-us'),
    path('course/', views.course, name='course'),
    path('course/<int:courseid>', views.coursedetail),
    path('form/', views.userForm),
    path('calculator/', views.calculator),
    path('evenodd/', views.evenodd, name='evenodd'),
    path('marksheet/', views.marksheet, name='marksheet'),
    path('newsdetail/<slug>', views.newsDetail),
    path('service/', views.service),
    path('enquire/', views.enquire, name='enquire'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)