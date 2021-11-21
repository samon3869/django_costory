from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.http import Http404
from django.views.generic import (
    CreateView, ListView, DetailView, UpdateView, DeleteView, RedirectView
)
from django.urls import reverse
from .models import Post
from .forms import PostForm

# Create your views here.

class PostListView(ListView):
    model = Post
    ordering = ['-dt_created']
    paginate_by = 6


class PostDetailView(DetailView):
    model = Post
    

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    
    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.id})
        
        
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    
    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.id})


class PostDeleteView(DeleteView):
    model = Post
    
    def get_success_url(self):
        return reverse('post-list')


# 이런 간단한 것은 함수형쓰는게 직관적이고 좋음
# generic view 수업이니까 다루는 것 뿐, 이렇게 하지 않아도 됨
# def index(request):
#     return redirect('post-list')
class IndexRedirectView(RedirectView):
    pattern_name = 'post-list'