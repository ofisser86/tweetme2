import random
from django.conf import settings
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url


from .forms import TweetForm

from .models import Tweet


ALLOWED_HOSTS = settings.ALLOWED_HOSTS


# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, 'templates/pages/home.html', context={}, status=200)


def tweet_create_view(request, *args, **kwargs):
    form = TweetForm(request.POST or None)
    next_url = request.POST.get('next') or None

    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if next_url is not None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        form = TweetForm()
    return render(request, 'components/form.html', context={'form': form})


def tweets_list_view(request, *args, **kwargs):
    """

     REST API view
     return json data
     """

    qs = Tweet.objects.all()
    tweet_list = [{'id': x.id, 'content': x.content, 'likes': random.randint(0, 159)} for x in qs]
    data = {
        'idUser': False,
        'response': tweet_list
    }
    return JsonResponse(data)


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """

    REST API view
    return json data
    """
    data = {
        'id': tweet_id,
        # 'image': obj.image.url
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except Exception:
        data['message'] = "Not found"
        # writes to headers status
        status = 404

    return JsonResponse(data, status=status)
