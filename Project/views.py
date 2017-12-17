from django.shortcuts import render
from .models import Book
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST', 'GET'])
def index(request, *args):
    if request.method == 'GET':
        return HttpResponse(u'GET')


def index2(request):
    return render(request, 'index.html')


@api_view(['POST', 'GET'])
def post(request):
    if request.method == 'POST':
        title = request.POST['title']
        author= request.POST['author']
        summary = request.POST['summary']
        Book(title=title, author=author, summary=summary).save()
        return HttpResponse(u'POST')