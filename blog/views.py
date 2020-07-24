from django.shortcuts import render, get_object_or_404
from django.utils import timezone 
from .models import Post,LineListing
from .forms import PostForm, LineListingForm 
from django.shortcuts import redirect 
from rest_framework import viewsets
from .serializers import LineListingSerializer

# Create your views here.
class LineListingViewSet(viewsets.ModelViewSet):
    queryset = LineListing.objects.all().order_by('village')
    serializer_class = LineListingSerializer
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blog/post_list.html',{'posts':posts})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request,'blog/post_detail.html', {'post':post})
def post_new(request):
    if request.method == "POST" :
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html',{'form': form})
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

def linelist_list(request):
    posts = LineListing.objects.all()
    return render(request,'blog/post_list.html',{'posts':posts})
def linelist_detail(request, pk):
    post = get_object_or_404(LineListing, pk=pk)
    return render(request,'blog/post_detail.html', {'post':post})
def linelist_new(request):
    if request.method == "POST" :
        form = LineListingForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('linelist_detail',pk=post.pk)
    else:
        form = LineListingForm()
    return render(request, 'blog/post_edit.html',{'form': form})
def linelist_edit(request, pk):
    post = get_object_or_404(LineListing, pk=pk)
    if request.method == "POST":
        form = LineListingForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('linelist_detail', pk=post.pk)
    else:
        form = LineListingForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


