from django.shortcuts import render

def base_fun(request):

    return render(request, "base/main_navbar.html")