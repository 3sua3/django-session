from django.urls import path
from blog import views

app_name = 'blog'
# 중복을 피하기 위한 url 네임스페이스
urlpatterns = [
    # /blog/
    path("", views.home, name="home"),
    path("new/", views.new, name="new"),
    path("detail/<int:post_pk>/", views.detail, name="detail"),
    path("update/<int:post_pk>/", views.update, name="update"),
    path("delete/<int:post_pk>/", views.delete, name="delete"),
    path("deleteComment/<int:post_pk>/<int:comment_pk>/", views.deleteComment, name="deleteComment"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
]