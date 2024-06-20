"""
URL configuration for pollingapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from pollapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    
    path('contact',views.contact,name="contact"),
    path('registerpage/',views.registerpage,name="registerpage"),
    path('loginpage/',views.loginpage,name="loginpage"),
    path('votingpage',views.votingpage,name="votingpage"),
    path("logoutpage",views.logoutpage,name="logoutpage"),
    path("admin_dashboard",views.admin_dashboard,name="admin_dashboard"),
    path("vote/<int:candidate_id>",views.vote,name="vote"),
    path("Feedback",views.Feedback,name="Feedback"),
    path('admin/', admin.site.urls),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
