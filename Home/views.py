from django.shortcuts import render,redirect


def index_view(request):

    return render(request,"Home/index.html")
