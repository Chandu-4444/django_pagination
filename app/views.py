from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator

def pagination(request):
    post_models = Post.objects.all()
    paginator = Paginator(post_models, 2)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    return render(request, 'index.html', {'page_objects': page_object})