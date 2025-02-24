from django.shortcuts import render, reverse, redirect, get_object_or_404

# Create your views here.
from .models import Board
# from django.urls import 
from .forms import CreateModelForm
from django.http import HttpResponse

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
        form = CreateModelForm()
        context = {
                    "form":form }
        return render(request,"ex_board/create.html", context)
    
    else:
        title = request.POST.get("title")
        author = request.POST.get("author")
        content = request.POST.get("content")
        Board(title=title,author=author,content=content).save()
        return redirect(reverse("ex_board:list"))
    
def boardupdate(request,id):
    board = Board.objects.get(pk=id)
    print(board)
    # return HttpResponse("테스트")
    if request.method == "GET":
        form = CreateModelForm(instance=board)
        context ={"form": form,
                  "object": board}
        return render(request,"ex_board/update.html", context)
    
    else:
        form = CreateModelForm(request.POST, instance=board)
        print(form)
        if form.is_valid():
            form.save()                            
            return redirect(reverse("ex_board:detail" , args=(board.id,)))
    
def boarddelete(request, id):
    object = Board.objects.get(id = id)
    if request.method == "GET":
        return render(request,"ex_board/delete.html", {"object":object})
    
    else:
        object.delete()
        return redirect(reverse("ex_board:list"))
    