from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *

# Create your views here.
class PostListView(ListView):
    model = Post
    context_object_name = "all_posts"
    def get_context_data(self, **kwargs):
        context = super(PostListView,
self).get_context_data(**kwargs)
        context['post_list'] = Post.objects.all()
        return context

class PostDetailView(DetailView):
    model = Post
    context_object_name = "all_posts"
    context_object_name = "post"
    def get_context_data(self, **kwargs):
        context = super(PostDetailView,
self).get_context_data(**kwargs)
        context['post_list'] = Post.objects.all()
        return context
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
                form.save()
                return redirect('success') 
    else:
        form = PostForm()
    return render(request, 'posts/post_add.html', {'form': form})

def success(request): 
    return HttpResponse('successfuly uploaded') 
    print("Success")
    
def filter_list(request):
    f = frontFilter(request.GET, queryset=filter.objects.all())
    return render(request, 'posts/filter.html', {'filter': f})