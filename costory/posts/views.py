from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.http import Http404
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse
from .models import Post
from .forms import PostForm

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    ordering = ['-dt_created']
    paginate_by = 6
    page_kwarg = 'page'
    

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'
    

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'
    
    def get_success_url(self):
        return reverse('post-detail', kwargs={'post_id': self.object.id})
        
        
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'
    pk_url_kwarg = 'post_id'
    
    def get_success_url(self):
        return reverse('post-detail', kwargs={'post_id': self.object.id})


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_confirm_delete.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'
    
    def get_success_url(self):
        return reverse('post-list')


def index(request):
    return redirect('post-list')