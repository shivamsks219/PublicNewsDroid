from tkinter import Image
from django.shortcuts import render
from app import logic
# Create your views here.

def index(request):
    return render (request, 'index.html')

def result(request):
    return render(request, 'display.html')

def uploadImage(request):
    if request.method == "POST":
        name = request.POST.get("name")
        comment = request.POST.get("comment")
        res = logic.check(comment)
        p = request.FILES['image']
        from .models import User
        user = User(pic = p)
        user.save()
        # img = User.objects.all()
        img_name = str(p)
        imgi = User.objects.all()
        imgres = logic.checkimg(p)

        data={
            'Name':name,
            'Comments':comment,
            'Sentiment':res,
            'imgSentiment':imgres,
            'img':img_name,
            'imgi':imgi,
        }
        return render (request, 'display.html', data)
