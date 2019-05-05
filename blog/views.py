from django.shortcuts import render,get_object_or_404,HttpResponse
from django.core.paginator import Paginator
from .models import BlogType,Blog,Comment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import re
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect
# Create your views here.
def blog_detail(request,id):
    blog = get_object_or_404(Blog,pk=id)
    context ={'blog':blog}
    return render(request,'detail.html',context)

#@login_required(login_url='/admin/login/')
def user_space(request,pk):
    user = get_object_or_404(User,pk=pk)
    context = {'myuser':user}
    return render(request,'user_space.html',context)

def blog_list_by_type(request,type): 
    page = request.GET.get('page',1)
    blogs = get_object_or_404(BlogType,blog_type=type).blog_set.all()
    paginator =  Paginator(blogs,10)
    page =  paginator.get_page(page)
    page_left = page.number - 2
    page_right = page.number + 7
    context={'page':page}
    context['page_left'] = page_left
    context['page_right'] = page_right
    return render(request,'blog_list.html',context)

def new_comment(request):
    if not request.user.is_authenticated:
        return HttpResponse("请登录")
    content = request.POST.get('content','notfound')
    partent_type = request.POST.get('parent','notfound')
    to_user = request.POST.get('to_user','notfound')
    object_id = request.POST.get('object_id','notfound')
    from_user = request.user
    if re.match(r'\w+',content) is None:
        return HttpResponse('评论内容不能为空')
    com = Comment()
    com.content_type = ContentType.objects.get(model=partent_type)
    com.object_id = int(object_id)
    com.from_user = request.user
    com.to_user = get_object_or_404(User,username = to_user)
    com.content = content
    com.save()
    referer =  request.META.get('HTTP_REFERER','/')
    return redirect(referer)
