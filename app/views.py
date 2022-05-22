from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse,JsonResponse
from app.models import *
from datetime import datetime
from django.views.decorators.cache import cache_control

# Create your views here.

@cache_control(no_cache=True, must_revalidate=True)
def index_page(request):
    return render(request,'index.html')

def register_page(request):
    return render(request,'register.html')

@cache_control(no_cache=True, must_revalidate=True)
def logout(request):
    try:
        now = datetime.now()
        now = now.strftime("%H:%M")
        user=User.objects.get(id=request.session['lid']).username
        content='%s logout at %s '%(user,now)
        obj=Activity(content=content)
        obj.save()
        request.session['lid']='logout'
        return render(request,'index.html')
    except Exception as e:
        print(e)
        return HttpResponse("<script>window.location.href='/index/'</script>")    

@cache_control(no_cache=True, must_revalidate=True)     
def register(request):
    name=request.POST['name']
    username=request.POST['username']
    password=request.POST['password']
    print(name)
    print(username)
    print(password)
    if User.objects.filter(username=username).exists():
        return HttpResponse("<script>alert('Username already exists');window.location.href='/register_page/'</script>")
    obj=User(name=name,username=username,password=password)  
    obj.save()  
    lid=obj.id
    request.session['lid']=lid
    now = datetime.now()
    now = now.strftime("%H:%M")
    user=username
    content='%s Signup at %s '%(user,now)
    obj=Activity(content=content)
    obj.save()
    return HttpResponse("<script>window.location.href='/home/'</script>")
    pass   


@cache_control(no_cache=True, must_revalidate=True)     
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        if User.objects.filter(username=username,password=password).exists():
            obj=User.objects.get(username=username)
            lid=obj.id
            request.session['lid']=lid
            now = datetime.now()
            now = now.strftime("%H:%M")
            user=username
            content='%s login at %s '%(user,now)
            obj=Activity(content=content)
            obj.save()
            return HttpResponse("<script>window.location.href='/home/'</script>")
        return HttpResponse("<script>alert('Invalid Login');window.location.href='/index/'</script>")    

@cache_control(no_cache=True, must_revalidate=True)     
def home(request):
    try:
        lid=request.session['lid']
        print(lid,'===')
        lid=int(lid)
        return render(request,'home.html')
    except Exception as e:
        print(e)
        return HttpResponse("<script>alert('please login');window.location.href='/index/'</script>") 

@cache_control(no_cache=True, must_revalidate=True)     
def add_message(request):
    user=User.objects.get(id=request.session['lid']).username
    msg=request.POST['content']
    obj=Message(content=msg,username=user)
    obj.save()
    now = datetime.now()
    now = now.strftime("%H:%M")
    user=User.objects.get(id=request.session['lid']).username
    content='%s Added a message at %s '%(user,now)
    obj=Activity(content=content)
    obj.save()
    return HttpResponse("<script>window.location.href='/home/'</script>")

@cache_control(no_cache=True, must_revalidate=True)     
def view_messages(request):
    try:
        lid=request.session['lid']
        print(lid,'===')
        lid=int(lid)
        obj=Message.objects.all().order_by('-id')
        return render(request,'messages.html',{'msg':obj}) 
    except Exception as e:
        print(e)
        return HttpResponse("<script>alert('please login');window.location.href='/index/'</script>") 



@cache_control(no_cache=True, must_revalidate=True)     
def delete_msg(request):
    id=request.GET.get('id')
    obj=Message.objects.get(id=id)
    obj.delete()
    now = datetime.now()
    now = now.strftime("%H:%M")
    user=User.objects.get(id=request.session['lid']).username
    content='%s Deleted a message at %s '%(user,now)
    obj=Activity(content=content)
    obj.save()
    return HttpResponse('Done')

@cache_control(no_cache=True, must_revalidate=True)     
def edit_msg_page(request):
    try:
        id=request.POST['id']
        obj=Message.objects.get(id=id)
        return render(request,'edit_page.html',{'obj':obj})
    except Exception as e:
        print(e)
        return HttpResponse("<script>alert('please login');window.location.href='/index/'</script>")    


@cache_control(no_cache=True, must_revalidate=True)     
def edit_msg(request):
    id=request.POST['id']
    content=request.POST['content']
    print(content,'content')
    print(id,'id')
    obj=Message.objects.get(id=id)
    obj.content=content
    obj.save()
    now = datetime.now()
    now = now.strftime("%H:%M")
    user=User.objects.get(id=request.session['lid']).username
    content='%s Edited a message at %s'%(user,now)
    print(content,'======')
    obj=Activity(content=content)
    obj.save()
    return HttpResponse("<script>window.location.href='/view_messages/'</script>")

@cache_control(no_cache=True, must_revalidate=True)     
def view_activities(request):
    try:
        obj=Activity.objects.all().order_by('-id')[:10]
        return render(request,'view_activites.html',{'obj':obj})
    except Exception as e:
        print(e)
        return HttpResponse("<script>alert('please login');window.location.href='/index/'</script>")    

@cache_control(no_cache=True, must_revalidate=True)     
def activity(request):
    qs=Activity.objects.all().order_by('-id')[:10]
    sqs=serializers.serialize('json',qs)    
    response={
        'data':sqs
    }
    #print(sqs)
    return JsonResponse(response)    