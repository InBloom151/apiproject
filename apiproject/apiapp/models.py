from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Пользователь', null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created', 'title']


class Comment(MPTTModel):
    text = models.TextField(verbose_name='Текст')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Пользователь', null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='Пост')
    parent = TreeForeignKey(
        'self',
        blank=True, null=True,
        on_delete=models.CASCADE,
        related_name='children',
        verbose_name='Родительский комментарий'
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created']

    class MPTTMeta:
        order_insertion_by = ['created']
