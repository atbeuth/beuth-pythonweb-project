from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from .forms import PostForm
# Create your views here.

class PostListView(ListView):
    model = Post
    context_object_name = "all_posts"
    def get_context_data(self, **kwargs):
        context = super(PostListView,
self).get_context_data(**kwargs)
        context['post_list'] = Post.objects.all()
        return context

# Create your views here.
class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    def get_context_data(self, **kwargs):
        context = super(PostDetailView,
self).get_context_data(**kwargs)
        context['post_list'] = Post.objects.all()
        return context
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
                form.save()
    else:
        form = PostForm()
    return render(request, 'posts/post_add.html', {'form': form})