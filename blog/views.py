from django.shortcuts import render
from django.utils import timezone
from .models import post

def post_list(request):
    qs = post.objects.all()
    qs = qs.filter(published_date=timezone.now())
    qs = qs.order_by('published_date')

    return render(request, 'blog/post_list.html', {
        'post_list': qs,
    })

