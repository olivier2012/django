from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request,"home.html",{})
    #return HttpResponse("<h1> Hello World </h1>")

def contact_view(request, *args, **kwargs):
    return render(request,"contact.html",{})

def about_view(request, *args, **kwargs):
    my_context ={
        "my_text": "first",
        "my_number": 123,
        "my_list": [111,222,333,444,5555,66]
    }
    return render(request,"about.html",my_context)
    #return HttpResponse("<h1> About page </h1>")

def video_view(request, *args, **kwargs):
    return render(request,"video.html",{})
    #return HttpResponse("<h1> video page </h1>")

def image_view(request, *args, **kwargs):
     return render(request,"image.html",{})
    #return HttpResponse("<h1> image page </h1>")