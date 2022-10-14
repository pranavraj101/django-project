from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('<h1>Welcome to the project</h1>')


def home(request):
    return HttpResponse('<h1>THis iS a HoMe pag0\e</h1>')

def hiname(request,name):
    return HttpResponse('<h2>Hi {}</h2>'.format(name))

def add(request,a,b):
    return HttpResponse("<h1>THe SuM of {} anD {} iS {}</h1>".format(a,b,int(a)+int(b)))


def temp_Demo(request):
    list=['apple','mango','banana','pineapple','grapes']
    return render(request,'template1.html',context={"name":"Pranav",'list':list})
    
def ghat(request):
    return render(request,'ghat.html')

def rmg(request):
    return render(request,'rmg.html')

def sarnath(request):
    return render(request,'sarnath.html')

def temple(request):
    return render(request,'temple.html')

def varanasi_tour(request):
    return render(request,'varanasi tourism.html')


def hometemp(request):
    return render(request,'pages/home.html')

def aboutus(request):
    return render(request,'pages/about.html')

def base(request):
    return render(request,'base.html')

from django.core.files.storage import FileSystemStorage
def form(request):
    if request.method=='POST':
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        cname=request.POST.get("cname")
        add=request.POST.get("add")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        details=request.POST.get("detials")
        acc=request.POST.get("acc")
        if request.FILES:
            files=request.FILES["profilepic"]
            fs=FileSystemStorage()
            savedfile=fs.save(files.name,files)
            file_url=fs.url(savedfile)
        
        return HttpResponse("<h1>Form Successfully Submited Data got is {} {} {} {} {} {} {} {} <img src='{}'> </h1>".format(fname,lname,cname,add,email,phone,details,acc,file_url))

    return render(request,'form.html')