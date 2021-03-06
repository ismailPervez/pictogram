from django.forms import ModelForm, CharField, PasswordInput, TextInput
from .models import User, Post, Comment

'''
ERRORS:
if you try to add another field that is not registered or is not in the model, then it will through an error (django.core.exceptions.FieldError: Unknown field(s) (password2) specified for User)
'''

class RegisterForm(ModelForm):
    confirm_password = CharField(widget=PasswordInput, label='confirm password')
    class Meta:
        model = User
        fields = ['username', 'email', 'bio', 'profile_pic', 'password', 'confirm_password']
        widgets = {
            'password': PasswordInput()
        }

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            self.add_error('confirm_password', 'passwords do not match')

        return cleaned_data

class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['picture', 'caption']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': ''
        }

        widgets = {
            'content': TextInput(attrs={'placeholder': 'post your comment...'})
        }
