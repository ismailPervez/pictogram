from django.urls import path
from users import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('post/', views.create_post, name='post'),
    path('profile/<username>/', views.user_profile, name='profile'),
    path('like/post/<post_id>/', views.like_post, name='like-post'),
    path('post/<post_id>/', views.get_full_post, name='full_post'),
    path('delete/comment/<comment_id>/', views.delete_comment, name='delete_comment'),
    path('posts/filtered/<query>/', views.search_post, name='search_posts'),
    path('follow/<username>/', views.follow_user, name='follow')
]