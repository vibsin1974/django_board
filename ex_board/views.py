from django.shortcuts import render, reverse, redirect

# Create your views here.
from .models import Board
# from django.urls import 

def boardlist(request):
    objects = Board.objects.order_by("-pk")
    return render(request,"ex_board/list.html",{"objects":objects})

def boarddetail(request, id):
    object = Board.objects.get(id=id)
    object.read_count +=1
    object.save()
    return render(request, "ex_board/detail.html", {"object":object})

def boardcreate(request):
    if request.method == "GET":
        return render(request,"ex_board/create.html")
    
    else:
        title = request.POST.get("title")
        author = request.POST.get("author")
        content = request.POST.get("content")
        Board(title=title,author=author,content=content).save()
        return redirect(reverse("ex_board:list"))
    
def boardupdate(request,id):
    object = Board.objects.get(id=id)

    if request.method == "GET":
        return render(request,"ex_board/update.html", {"object":object})
    
    else:
        object.title = request.POST["title"]
        object.author = request.POST["author"]
        object.content = request.POST["content"]
        object.save()                                                           
        return redirect(reverse("ex_board:list"))
    
def boarddelete(request, id):
    object = Board.objects.get(id = id)
    if request.method == "GET":
        return render(request,"ex_board/delete.html", {"object":object})
    
    else:
        object.delete()
        return redirect(reverse("ex_board:list"))
    