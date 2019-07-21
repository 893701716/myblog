from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
# Create your views here.
import  datetime
from .models import  Visitor
def index(request):
    return render(request, 'newapp/index.html')
def registered(request):
    name = request.POST.get('name')
    gender = request.POST.get('gender')
    age = request.POST.get('age')
    number = request.POST.get('number')
    password=request.POST.get('password2')
    try:
       existuser=Visitor.objects.get(number=number)
       if existuser:
           return  render(request,'newapp/tipofexisted.html')
    except:
          visitor = Visitor()
          visitor.name = name
          visitor.gender = gender
          visitor.age = age
          visitor.number = number
          visitor.password=password
          visitor.save()
          return render(request, 'newapp/registered.html', {
                'name': name,
                'number': number
            })
from newapp.models import Message
def login(request):
    password=request.POST.get('password')
    usernumber=request.POST.get('number')
    try:
        visitor = Visitor.objects.get(password=password,number=usernumber)
        if visitor:
            request.session['name']=visitor.name
            return render(request, 'newapp/blogPage.html')
    except:
        return render(request, 'newapp/failLogin.html')
def registry(request):
    return render(request, 'newapp/registry.html')
def blogPage(request):
    return render(request, 'newapp/blogPage.html')
def pannelpage(request):
    messagelist=Message.objects.all().order_by('-pubtime')
    paginator =Paginator(messagelist,2)
    page=request.GET.get('page')#获取页数 默认基于第一页
    print(page)
    mess=paginator.get_page(page) #返回当前页
    print('mess：',mess)
    return render(request, 'newapp/pannelpage.html', {
        'messagelist':messagelist,
        'mess':mess,
    })
def writepage(request):
    return render(request, 'newapp/writepage.html')
def savemessage(request):
    text=request.POST.get('text')
    title=request.POST.get('caption')
    name = request.session.get('name')
    m=Message()
    m.username=name
    m.leavemessage=text
    m.title=title
    m.pubtime=datetime.datetime.now()
    try:
        file = request.FILES.getlist('file')
        for f in file:
            m.image = f
        m.save()
    except:
        m.image=''
        m.save()
    return render(request, 'newapp/launchSuccessfully.html')
def personalpage(request):
    name=request.session.get('name')
    allmessage=Message.objects.filter(username=name).order_by('-pubtime')
    pagintor=Paginator(allmessage,1)
    page = request.GET.get('page')
    allpage=pagintor.get_page(page)
    return render(request, 'newapp/personalpage.html', {
            'name': name,
        'allmessage':allmessage,
        'allpage':allpage
        })
