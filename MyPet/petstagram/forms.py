from django import forms
from .models import Feed

class FeedForm(forms.ModelForm):
    body = forms.CharField(required=True,
            widget=forms.widgets.Textarea(attrs={
                "placeholder": "설명을 입력하세요...",
                "class": "textarea is-success is-medium",
            }
        ),
        label="",)


    class Meta:
        model = Feed
        exclude = ("user", )