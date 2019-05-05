from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    path('<int:id>/',views.blog_detail,name = 'blog_detail'),
    path('user/<int:pk>/',views.user_space,name = 'user_space'),
    path('blog_list/type/<str:type>',views.blog_list_by_type,name = 'blog_list_by_type'),
    path('comment/',views.new_comment,name = 'new_comment'),
]