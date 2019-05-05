from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation
# Create your models here.
class BlogType(models.Model):
    blog_type = models.CharField('分类',max_length=30)
    def __str__(self):
        return self.blog_type

class Comment(models.Model):
    content = models.TextField('评论',default = '')
    content_type = models.ForeignKey(ContentType,on_delete = models.CASCADE)
    object_id =models.PositiveIntegerField()
    from_user = models.ForeignKey(User,on_delete=models.CASCADE,null = True,default=None,related_name = 'from_user')
    to_user = models.ForeignKey(User,on_delete=models.CASCADE,null = True,default=None,related_name = 'to_user')
    content_object = GenericForeignKey('content_type','object_id')
    created_time = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.content
    def get_comment(self):
        contenttype =  ContentType.objects.get_for_model(self)
        subcomments =  Comment.objects.filter(content_type=contenttype,object_id=self.pk)
        print(subcomments)
        return subcomments
    class Meta:
        ordering = ['-created_time']


class Blog(models.Model):
    title = models.CharField('标题',max_length=100)
    author = models.ForeignKey(User,on_delete = models.CASCADE,null=True)
    blog_type = models.ForeignKey(BlogType,on_delete=models.SET_NULL,null=True)
    content = models.TextField('内容',default = '')
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    comments = GenericRelation(Comment,related_query_name='blog')
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_time']

