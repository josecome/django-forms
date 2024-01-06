from django.shortcuts import render, redirect
from app.forms import PostForm
from app.models import Post
from datetime import datetime
from django.http import HttpResponse

# Create your views here.

def home_view(request):
    form = PostForm()
    Posts = Post.objects.all()
    return render(
        request, 'home.html', 
        {'form': form, 'posts': Posts}
)


def add_new_post_view(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            #form.save()
            try:
                form = form.save(commit=False)
                form.user_id = 1
                form.date_created = datetime.now()
                form.save()
                return redirect('/')
            except Exception as e:
                return HttpResponse(e)
        else:
            pass
    else:
        return redirect('/')

    