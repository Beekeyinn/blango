import json
from http import HTTPStatus

from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from blog.models import Post


def post_to_dict(post):
  return {
    "pk": post.pk,
    "author_id": post.author,
    "created_at": post.created_at,
    "modified_at": post.modified_at,
    "title": post.title,
    "slug": post.slug,
    "summary": post.summary,
    "content": post.content,
  }
from blog.api.serializers import PostSerializer


@csrf_exempt
def post_list(request):
  if request.method == "GET":
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return JsonResponse({"data":serializer.data})
  elif request.method == "POST":
    data = json.loads(request.body)
    serializer = PostSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    post = serializer.save()
    return HttpResponse(
      status=HTTPStatus.CREATED,
      headers = {"Location":reverse("api_post_detail",args=(post.pk,))},
    )
  return HttpResponseNotAllowed(["GET","POST"])

def post_detail(request, pk):
  post = get_object_or_404(Post, pk=pk)
  if request.method == "GET":
    return JsonResponse(PostSerializer(post).initial_data)
  elif request.method == "PUT":
    serializer = PostSerializer(post,data=json.loads(request.body))
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return HttpResponse(status=HTTPStatus.NO_CONTENT)
  elif request.method=="DELETE":
    post.delete()
    return HttpResponse(status=HTTPStatus.NO_CONTENT
    )
  return HttpResponseNotAllowed(["GET","PUT","DELETE"])
