from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.

def middleware_test(request):
    """
    Sample用ビュー
    """
    print("Sample用ビューの処理")
    return HttpResponse('Middlewareのテスト')