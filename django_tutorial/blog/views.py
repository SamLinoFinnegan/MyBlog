from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from users.models import Profile
from .models import Post
from django.contrib.auth.models import User

def welcome_view(request):
 
    context = {
        "title":"Welcome to my blog"
    }
    return render(request, "blog/welcome_blog.html", context)

def about(request):
    context = {
        "title":"About"
    }
    return render(request, "blog/about.html", context)

class Home(ListView):
    model = Post
    template_name = "blog/home.html"
    ordering = ["-date_posted"]
    context_object_name = 'posts'
    paginate_by = 5


class PostUser(ListView):
    model = Post
    template_name = "blog/post_user.html"
    ordering = ["-date_posted"]
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        profile = Profile.objects.get(user=user)
        context['user_profile'] = profile
        return context
    


class PostPage(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "blog/post_page.html"
    
    def get(self,request, *args, **kwargs):

        pk = self.kwargs.get('pk')

        context = {
            "title":"Post page",
            "post":self.model.objects.get(pk=pk)
        }
        return render(request, self.template_name, context)


class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "blog/new_post.html"
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "blog/new_post.html"
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        else:
            return False
        
class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/delete_post.html"
    success_url = "/"


    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        else:
            return False
