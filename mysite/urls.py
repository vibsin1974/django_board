from django.contrib import admin
from django.urls import path, include
# from ex_board import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', include("ex_board.exurls"))
]
