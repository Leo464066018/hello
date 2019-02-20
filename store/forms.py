from django import forms
from django.contrib.auth import authenticate, login
from .models import Operation, Item, PostManage


class LoginForm(forms.Form):
    username = forms.CharField(
        label="用户名",
        max_length=12,
        min_length=3,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入用户名', })
        )
    password = forms.CharField(
        label="密码", 
        max_length=12, 
        min_length=3, 
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请输入密码', })
        )

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError('用户名或密码不正确')
        else:
            self.cleaned_data['user'] = user
        return self.cleaned_data


# class OperateForm(forms.Form):
#     item = forms.ModelChoiceField(
#         queryset=Item.objects.all(),
#         label=False,
#         empty_label='请选择配件'
#     )
class OperateForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = ('item', 'operate', 'num')
        widgets = {
            'item': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'operate': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'num': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete': 'off',
                }
            ),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = PostManage
        fields = ('post_num', 'server_type', 'server_num', 'note_text')
        widgets = {
            'post_num': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete': 'off',
                }
            ),
            'server_type': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'server_num': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete': 'off',
                }
            ),
            'note_text': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            )
        }