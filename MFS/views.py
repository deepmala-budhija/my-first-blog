from django.shortcuts import render, get_object_or_404
from django.utils import timezone 
from .models import MFS
from .forms import PostForm 
from django.shortcuts import redirect 

# Create your views here.
def post_list(request):
    posts = MFS.objects.filter(house_number__lte=500).order_by('house_number')
    return render(request,'mfs/post_list.html',{'posts':posts})
def post_detail(request, pk):
    post = get_object_or_404(MFS, pk=pk)
    return render(request,'mfs/post_detail.html', {'post':post})
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
    return render(request, 'mfs/post_edit.html',{'form': form})
def post_edit(request, pk):
    post = get_object_or_404(MFS, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'mfs/post_edit.html', {'form': form})

