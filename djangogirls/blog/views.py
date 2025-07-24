from django.shortcuts import render, get_object_or_404  
from django.utils import timezone
#include the code from model in models.py by typing the code on line 3
from .models import Post #the dot before models means current directory or application
from .forms import PostForm #import PostForm from forms.py file in the same directory
from django.shortcuts import redirect

# Create your views here.
#views connect models and templates 
#need to take the models we want to display in our post_list view and pass them to the template 


def post_list(request,):
    #create a variable for our query set called posts/ name of queryset = posts
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts}) #render function has one parameter = request(everything from the user via the internet) and another giving the template file ('blog/post_list.html')
#created a def function called post_list that takes request and will return the value it gets from calling render function 
#render function will put together our template 

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})





























































































