from django.forms import ModelForm, BooleanField  # Импортируем true-false поле
from .models import Post


class PostForm(ModelForm):
    check_box = BooleanField(label='Алло, Галочка!')  # добавляем галочку или же true-false поле
    class Meta:
        model = Post
        fields = ['author', 'title', 'categoryType', 'postCategory']
