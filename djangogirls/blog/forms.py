from django import forms #import forms from django library
from .models import Post #import Post model from models.py file in the same directory

# Create a form for the Post model
#this form will be used to create and edit posts in the admin interface
class PostForm(forms.ModelForm): #forms.ModelForm tells django that this form is based on a model
    #Meta class is used to specify the model and fields that the form will use

    class Meta:
        model = Post
        fields = ('title', 'text') 
