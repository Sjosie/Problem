from django import forms
from .models import Post
from .models import VideoPost
from ckeditor.widgets import CKEditorWidget


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)



class VideoForm(forms.ModelForm):
    class Meta:
        model= VideoPost
        fields= ["name", "videofile"]


class PostEditForm(forms.Form):
    content = forms.CharField(widget=CKEditorWidget, label='')