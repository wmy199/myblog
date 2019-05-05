from django.contrib import admin
from .models import Blog ,BlogType,Comment
# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','title','content','created_time','update_time')


@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('blog_type',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content_type','content_object',)