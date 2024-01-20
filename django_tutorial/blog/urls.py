from django.urls import path
from . import views



urlpatterns = [
    path("", views.welcome_view, name="blog-welcome"),
    path("home/", views.Home.as_view(), name="blog-home"),
    path("post/<int:pk>/", views.PostPage.as_view(), name="blog-post"),
    path("post/new/", views.CreatePost.as_view(), name="blog-post-create"),
    path("post/<int:pk>/update/", views.UpdatePost.as_view(), name="blog-post-update"),
    path("post/<int:pk>/delete/", views.DeletePost.as_view(), name="blog-post-delete"),
    path("user/<str:username>", views.PostUser.as_view(), name="blog-post-user"),
    path("about/", views.about, name="blog-about"),
]
