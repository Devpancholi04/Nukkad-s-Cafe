from django.shortcuts import render

def base_fun(request):

    return render(request, "home/home.html")