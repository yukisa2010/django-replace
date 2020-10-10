from django import forms
from django.core.exceptions import ValidationError


widget_textarea = forms.Textarea(
    attrs={
        "class":"form-control"
    }
)
widget_textinput = forms.TextInput(
    attrs={
        "class":"form-control"
    }
)


class TextForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label="")
    search = forms.CharField(label="検索", widget=widget_textinput)
    replace = forms.CharField(label="置換", widget=widget_textinput)

    def clean(self):
        # djangoもともとのバリデーションを実行してデータを取得
        data = super().clean()
        text = data["text"]
        if len(text) <= 5:
            raise ValidationError("テキストが短すぎます。")
        # 最後は必ずデータ全体を返します
        return data
    
        
# from .models import Post

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title', 'body']
        
        
        
        