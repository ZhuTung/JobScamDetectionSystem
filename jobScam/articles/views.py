from django.shortcuts import render

# Create your views here.
def article1(request):
    return render(request, "articles/article1.html")

def article2(request):
    return render(request, "articles/article2.html")

def article3(request):
    return render(request, "articles/article3.html")

def article4(request):
    return render(request, "articles/article4.html")