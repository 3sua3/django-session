"""blogProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from blogApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('new', views.new, name = 'new'),
    path('', views.list, name = 'list'),
    path('detail/<int:article_id>', views.detail, name = 'detail'),
    path('recomment/<int:article_id>/<int:comment_id>/', views.recomment, name = 'recomment'),
    path('delete-comment/<int:article_id>/<int:comment_id>', views.delete_comment, name = 'delete-comment'),
    path('delete-recomment/<int:article_id>/<int:comment_id>/<int:recomment_id>', views.delete_recomment, name = 'delete-recomment'),
    path('category/<str:category_name>', views.category, name = 'category'),
    path("registration/signup/", views.signup, name="signup"),
    path("registration/login/", views.login, name="login"),
    path("registration/logout/", views.logout, name="logout"),
    path('accounts/', include('allauth.urls')),
]