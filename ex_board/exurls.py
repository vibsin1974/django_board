from django.urls import path
from . import views
app_name="ex_board"
urlpatterns =[
    path("",views.boardlist, name="list"),
    path("detail/<int:id>/", views.boarddetail, name="detail"),
    path("create/", views.boardcreate, name="create"),
    path("update/<int:id>/", views.boardupdate, name="update"),
    path("delete/<int:id>/", views.boarddelete, name="delete")
        
]