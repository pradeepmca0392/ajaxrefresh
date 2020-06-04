from django.shortcuts import render
from django.http import JsonResponse
from .models import Post

def create_post(request):
    posts = Post.objects.all()
    response_data = {}

    if request.POST.get('action') == 'post':
        book = request.POST.get('book')
        author = request.POST.get('author')
        description = request.POST.get('description')

        response_data['book'] = book
        response_data['author'] = author
        response_data['description'] = description

        Post.objects.create(
            book=book,
            author=author,
            description=description,
            )
        return JsonResponse(response_data)
    return render(request, 'create_post.html', {'posts': posts})
