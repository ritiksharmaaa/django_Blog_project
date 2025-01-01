"""
URL configuration for Blog project.

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
from django.urls import path , include 
from Blogpost import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("__debug__/", include("debug_toolbar.urls")),

    path('', views.home , name="home"),
    path('about/', views.about , name="about"),
    path('contact/', views.contact , name="contact"),
    path('singin/', views.login_user , name="login"),
    path('signup/', views.register , name="signup"),
    path('logout/', views.logout , name="logout"),
    path('blog/<int:id>/', views.detail_blog , name="visit"),
    path('dashboard/', views.dashboard , name="dashboard"),
    path('post-create/', views.createPost , name="create-post"),
    path('post-update/<int:id>/', views.update_post , name="dashboard-update-post"),
    path('post-delete/<int:id>/', views.delete_post , name="dashboard-delete-post"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# D:\programing\django\project\Blog>
