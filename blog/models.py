from django.db import models

from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    title = models.CharField('название статьи',max_length = 200)
    text = models.TextField('текст статьи')
    created_date = models.DateTimeField('дата создания',default = timezone.now())
    published_date = models.DateTimeField('дата публикации',blank = True,null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    author = models.CharField('имя автора',max_length=200)
    text = models.TextField('текст комментария')
    created_date = models.DateTimeField('дата публикации',default=timezone.now())
    approved_comment = models.BooleanField('одобрение комментария',default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    class Meta():
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
