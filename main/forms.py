from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from main.models import Post


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "text", "image", "author"]
        widgets = {
            "author": forms.HiddenInput(),
            "text": forms.Textarea()
        }


class RegisterForm(forms.Form):
    login = forms.CharField(max_length=64)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    repeat_password = forms.CharField(widget=forms.PasswordInput)

    def clean_login(self):
        if User.objects.filter(username=self.cleaned_data["login"]).exists():
            raise ValidationError("User already exists!")
        return self.cleaned_data["login"]

    def clean_repeat_password(self):
        if self.cleaned_data["password"] != self.cleaned_data["repeat_password"]:
            raise ValidationError("Passwords must match!")
        return self.cleaned_data["repeat_password"]


class CreateCommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
