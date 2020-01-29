from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post

# Create your views here.

class PostListView(ListView):
    model = Post
    paginate_by = 3

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'context']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'context']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def contact(request, author):
    get_author = User.objects.get(username=author)
    return render(request, 'main/contact.html', {'author': get_author})

class PostListMyViews(ListView):
    model = Post
    paginate_by = 5
    template_name = 'main/post_my_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)
