from django.shortcuts import render


def homepagemessage(request):
    return render(request,'index.html')