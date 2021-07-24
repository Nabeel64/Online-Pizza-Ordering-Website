from django.shortcuts import render,redirect
from django.http import HttpResponse
from PizzaApp.models import User,Pizzas,Cart,Order,Orderhistory
from PizzaApp.forms import Signup,PizzaForm,PfupForm,chgepwd
from django.contrib.auth import login


def home(request):
    return render(request,'html/home.html')

def signup(request):
    if request.method == 'POST':
        a = Signup(request.POST, request.FILES)
        if a.is_valid():
            a.save()
            return redirect('/login') 
    a = Signup()
    return render(request, 'html/signup.html', {'d':a})

def itlist(request):
    s=Pizzas.objects.all()
    if request.method == 'POST':
        a = PizzaForm(request.POST, request.FILES)
        if a.is_valid():
            a.save()
            return redirect('/itemlist')
    a = PizzaForm()
    return render(request,'html/itemlist.html',{'k':a,'p':s})

def itemdel(request,n):
    v = Pizzas.objects.get(id=n)
    if request.method == "POST":
        v.delete()
        return redirect('/itemlist')
    return render(request,'html/itdelete.html',{'q':v})

def itemup(request,m):
    k=Pizzas.objects.get(id=m)
    if request.method=="POST":
        e=PizzaForm(request.POST,request.FILES,instance=k)
        if e.is_valid():
            e.save()
            return redirect('/itemlist')
    e=PizzaForm(instance=k)
    return render(request,'html/itemupdate.html',{'x':e})

def vegmenu(request):
    a = Pizzas.objects.filter(pcategory='VG')
    if request.method=="POST":
        pn=request.POST['pizzaname']
        pt=request.POST['size']
        li=pt.split(" ")
        psize=li[0]
        pcost=int(li[1])
        k=Cart(pname=pn,psize=psize,pcost=pcost,uid_id=request.user.id)
        k.save()
        return redirect('/vm')
    return render(request, 'html/vegmenu.html', {'q': a})

def nvegmenu(request):
    a = Pizzas.objects.filter(pcategory='NV')
    if request.method=="POST":
        pn=request.POST['pizzaname']
        pt=request.POST['size']
        li=pt.split(" ")
        psize=li[0]
        pcost=int(li[1])
        k=Cart(pname=pn,psize=psize,pcost=pcost,uid_id=request.user.id)
        k.save()
        return redirect('/nvm')
    return render(request, 'html/nonvegmenu.html', {'q': a})

def cart(request):
    k=Cart.objects.filter(uid_id=request.user.id)
    p=Cart.objects.filter(uid_id=request.user.id).count()
    return render(request,'html/cart.html',{'s':k,'t':p})

def cartdel(request,m):
    v=Cart.objects.get(id=m)
    v.delete()
    return redirect('/ct')
    return render(request,'html/cart.html')

def bill(request):
    k=Cart.objects.filter(uid_id=request.user.id)
    tc=0
    for i in k:
        tc=tc+i.pcost
    if request.method == "POST":
        un=request.POST['name']
        mobilenumber=request.POST['mnumb']
        address=request.POST['address']
        string=""
        for i in k:
            string=string+i.pname+"("+i.psize+")"+","
        s=Order(uname=un,mnumb=mobilenumber,pizzas=string,tcost=tc,address=address)
        p=Orderhistory(pizzas=string,tcost=tc,address=address,uid_id=request.user.id)
        p.save()
        s.save()
        k.delete()
        return redirect('/')
    return render(request,'html/billing.html',{'o':k,'c':tc})

def orders(request):
    k=Order.objects.all()
    p=Order.objects.all().count()
    return render(request,'html/orders.html',{'s':k,'c':p})

def orderdel(request,m):
    k=Order.objects.get(id=m)
    k.delete()
    return redirect('/order')
    return render(request,'html/orders.html')

def history(request):
    k=Orderhistory.objects.filter(uid_id=request.user.id)
    p=Orderhistory.objects.filter(uid_id=request.user.id).count()
    return render(request,'html/Orderhistory.html',{'s':k,'c':p})

def pfle(request):
    return render(request,'html/profileview.html')

def profupdt(request):
    d=User.objects.get(id=request.user.id)
    if request.method=="POST":
        pf=PfupForm(request.POST,request.FILES,instance=d)
        if pf.is_valid():
            pf.save()
            return redirect('/pf')
    pf=PfupForm(instance=d)
    return render(request,'html/profileupdate.html',{'k':pf})

def changepwd(request):
    if request.method=="POST":
        k=chgepwd(user=request.user,data=request.POST)
        if k.is_valid():
            k.save()
            return redirect('/login')
    k = chgepwd(user=request)
    return render(request,'html/changepwd.html',{'t':k})