from django.shortcuts import render , redirect

# Create your views here.

from .form import *
from django.contrib.auth import logout



def logout_view(request):
    logout(request)
    return redirect('/')


def home(request):
    context = {'blogs' : BlogModel.objects.all()}
    return render(request , 'home.html' , context)

def login_view(request):
    return render(request , 'login.html')

def blog_detail(request , slug):
    context = {}
    try:
        blog_obj = BlogModel.objects.filter(slug = slug).first()
        context['blog_obj'] =  blog_obj
    except Exception as e:
        print(e)
    return render(request , 'blog_detail.html' , context)


def see_blog(request):
    context = {}
    
    try:
        blog_objs = BlogModel.objects.filter(user = request.user)
        context['blog_objs'] =  blog_objs
    except Exception as e: 
        print(e)
    
    print(context)
    return render(request , 'see_blog.html' ,context)


def add_blog(request):
    context = {'form' : BlogForm}
    try:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            print(request.FILES)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user
            
            if form.is_valid():
                content = form.cleaned_data['content']
                mode = form.cleaned_data['mode']
            
            blog_obj = BlogModel.objects.create(
                user = user , title = title, 
                content = content, image = image, mode=mode
            )
            print(blog_obj)
            return redirect('/add-blog/')
            
            
    
    except Exception as e :
        print(e)
    
    return render(request , 'add_blog.html' , context)


def blog_update(request , slug):
    context = {}
    try:
        blog_obj = BlogModel.objects.get(slug = slug)
       
        
        if blog_obj.user != request.user:
            return redirect('/')
        
        initial_dict = {'content': blog_obj.content,'mode':blog_obj.mode}
        form = BlogForm(initial = initial_dict)
        if request.method == 'POST':
            form = BlogForm(request.POST)
            print(request.FILES)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user
            b_obj = BlogModel.objects.filter(id = blog_obj.id)
            b_obj.delete()
            
            if form.is_valid():
                content = form.cleaned_data['content']
                mode = form.cleaned_data['mode']
            
                blog_obj = BlogModel.objects.create(slug = slug,
                    user = user , title = title, 
                    content = content, image = image, mode=mode
                )

        context['blog_obj'] = blog_obj
        context['form'] = form
        context['image1'] = blog_obj.image
    except Exception as e :
        print(e)

    return render(request , 'update_blog.html' , context)


def blog_delete(request , id):
    try:
        blog_obj = BlogModel.objects.get(id = id)
        
        if blog_obj.user == request.user:
            blog_obj.delete()
        
    except Exception as e :
        print(e)

    return redirect('/see-blog/')


def  register_view(request):
    return render(request , 'register.html')



def verify(request,token):
    try:
        profile_obj = Profile.objects.filter(token = token).first()
        
        if profile_obj:
            profile_obj.is_verified = True
            profile_obj.save()
        return redirect('/login/')

    except Exception as e : 
        print(e)
    
    return redirect('/')