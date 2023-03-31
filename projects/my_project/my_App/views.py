from django.shortcuts import render
from django.http import response, HttpResponse
from django.views.generic import TemplateView
from .models import Post

# Create your views here.
def homepageView(request):
    return render(request, "homo.html",{"name":Post.text})
# Create your views here.
def second_View(request):
    return render(request, "uwu.html",{"name":"secondary"})