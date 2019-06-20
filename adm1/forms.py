from django import forms
from .models import Post
from .models import VideoPost
from ckeditor.widgets import CKEditorWidget
from tinymce import TinyMCE


class PostForm(forms.ModelForm):

    # content = forms.CharField(
    #     widget = TinyMCEWidget(
    #         attrs = {'required': False, 'cols': 30, 'rows': 10}
    #     )
    # )

    class Meta:
        model = Post
        # fields = ('title', 'text',)
        fields = '__all__'

    

    # class Meta:
    #     model = Post
    #     fields = '__all__'




class VideoForm(forms.ModelForm):
    class Meta:
        model= VideoPost
        fields= ["name", "videofile"]


class PostEditForm(forms.Form):
    content = forms.CharField(widget=CKEditorWidget, label='')



