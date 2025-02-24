from django import forms
from .models import Board

class CreateModelForm(forms.ModelForm):
    class Meta:
        model = Board 
        fields = ["title","author", "content"]
        
        labels ={
                "title":"제목",
                "author":"작성자",
                "content":"내용"
        }