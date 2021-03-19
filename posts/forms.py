from django.forms import ModelForm, Textarea
from django.utils.translation import gettext_lazy as _

from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'group']
        labels = {
            'text': _('Текст'),
            'group': _('Группа')
        }
        help_texts = {
            'group': _('Выберите группу (необязательно)')
        }
        widgets = {
            'text': Textarea(attrs={'placeholder': _('Введите текст')})
        }
