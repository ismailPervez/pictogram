from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CommentForm, RegisterForm, CreatePostForm
from .models import Post, User, Like, Comment, UserFollowing
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.urls import reverse

def home(request):
    posts = Post.objects.order_by('date_posted').all()
    return render(request, 'users/index.html', {'posts': posts})

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            # form.save()
            new_user = User(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                profile_pic=form.cleaned_data['profile_pic'],
                password=make_password(form.cleaned_data['password'])
            )
            new_user.save()
            messages.success(request, 'Registration suceessful. You can now login')
            redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})

@login_required
def create_post(request):
    if request.method == "POST":
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = Post(
                picture=form.cleaned_data['picture'],
                caption=form.cleaned_data['caption'],
                user=request.user
            )

            new_post.save()
            messages.success(request, 'post successfully uploaded')

    else:
        form = CreatePostForm()

    return render(request, 'users/post.html', {'form': form})

def user_profile(request, username):
    user = User.objects.get(username=username)
    if not user:
        return HttpResponse('user not found. 404 error')

    posts = Post.objects.filter(user=user).all()
    print(user.is_followed(request.user.pk))

    return render(request, 'users/profile.html', {'profile_user': user, 'posts': posts})

@login_required
def like_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    if not post:
        return JsonResponse({'msg': 'post liked', 'status_code': 200})
    
    like = Like.objects.filter(user=request.user, post=post)
    if not like:
        like = Like(user=request.user, post=post)
        like.save()
        return JsonResponse({'msg': 'liked', 'status_code': 200})

    else:
        like.delete()
        return JsonResponse({'msg': 'unliked', 'status_code': 204})

def get_full_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                new_comment = Comment(
                    content=form.cleaned_data['content'],
                    user=request.user,
                    post=post
                )
                new_comment.save()

                form = CommentForm()

        else:
            messages.info(request, 'You need to be logged in to comment')
    
    else:
        form = CommentForm()
        
    return render(request, 'users/post_detail.html', {'post': post, 'form': form})

# delete comment
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return JsonResponse({'msg': 'comment deleted', 'status_code': 200})

# search functionality
def search_post(request, query):
    posts = Post.objects.all()
    filtered_posts = []
    for post in posts:
        if query in post.caption.lower() or query in post.user.username:
            filtered_posts.append(post)

    return render(request, 'users/results.html', {'posts': filtered_posts})

# follow a user
def follow_user(request, username):
    current_user = request.user
    followed_user = get_object_or_404(User, username=username)
    if followed_user.is_followed(current_user=current_user):
        # already exits as a follower of username
        # remove/unfollow
        print(followed_user.is_followed(current_user=current_user))
        UserFollowing.objects.filter(user=current_user, following_user=followed_user).delete()

        return redirect(reverse('profile', kwargs={'username': username}))

    else:
        print(followed_user.is_followed(current_user=current_user))
        new_follower = UserFollowing(user=current_user, following_user=followed_user)
        new_follower.save()
        
        return redirect(reverse('profile', kwargs={'username': username}))
