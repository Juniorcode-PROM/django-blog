"""
URL configuration for django_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from django_blog import settings
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', views.list_posts_view),
    path('posts/create/', views.create_post_view),
    path('posts/<int:post_id>/', views.get_post_view),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('register/', views.register_view),
    path('', views.home_view),
    path('posts/<int:post_id>/comment/', views.create_comment_view)
] + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
