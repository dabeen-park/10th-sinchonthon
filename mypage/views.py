from django.shortcuts import render

# Create your views here.

def mypage(request):
    return render(request, 'mypage.html')

def mypage2(request):
    return render(request, 'mypage2.html')

def mypage3(request):
    return render(request, 'mypage3.html')

def sinchong(request):
    return render(request, 'sinchong.html')

def sinchong2(request):
    return render(request, 'sinchong2.html')