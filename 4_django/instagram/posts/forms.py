from django import forms
from .models import Post
from .models import Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['content', 'image' ] # 어떤내용 보여줄지 설정하는 것


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = '__all__'
        fields = ['content']
# 댓글은 어디에 위치하면 좋을지 고민해보자