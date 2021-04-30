from django.shortcuts import render , redirect
from data.models import Developer,Technology,Domain,QA,Blog

from  django.contrib.auth.decorators import login_required

from .models import  Developer
from .forms import DeveloperForm ,SearchForm

from django.contrib import messages

# from data import forms

# Create your views here.


def index(request):
    return render(request,"base.html")

@login_required
def display(request):
    data = Developer.objects.all()
    # person = Developer.objects.get(technology__name="Java")
    # print(person)
    technologies = Technology.objects.all()
    domains=Domain.objects.all()
    blogs=Blog.objects.all()
    qas =  QA.objects.all()
    context={
        "data":data
    }

    # for developer in data:
    #     for tech in developer.technology.all():
    #         print(tech)
    return render(request , "data.html" , context)

# def DeveloperForm(request):
# 	form=forms.DeveloperForm()
# 	if request.method=='POST' :
# 		form=forms.DeveloperForm(request.POST)
# 		if form.is_valid() :
# 			print("In is valid part")
# 			p_rating=0
# 			b_rating=0
# 			q_rating=0
# 			t=form.cleaned_data['project']
# 			for x in t :
# 				p_rating=x.rating
# 			t=form.cleaned_data['blog']
# 			for x in t :
# 				b_rating=x.rating
# 			t=form.cleaned_data['q_a']
# 			for x in t :
# 				q_rating=x.rating
# 			print("rating ",p_rating,q_rating,b_rating)
# 			score=gen_score(q_rating,b_rating,p_rating)
# 			print("score by function",score)
# 			form.cleaned_data['score']=score
# 			messages.success(request,"Developer Added Succesfully")
# 			print(form.cleaned_data)
# 			form.save()
# 			print("Record inserted Succesfully.....!")
# 			return render(request,'AddDev/thank.html')
# 	return render(request,'AddDev/test.html',{'form':form})
# def DeveloperForm(request):
# 	form=forms.DeveloperForm()
# 	if request.method=='POST' :
# 		form=forms.DeveloperForm(request.POST)
# 		if form.is_valid() :
# 			print("In is valid part")
# 			form.save()
            
# 			print(form.cleaned_data)
# 			print("Record inserted Succesfully.....!")
# 	return render(request,'data/add_dev.html',{'form':form})

def gen_score(q,b,p):
	temp=(q*20 + b*30 + p*50)/100
	return temp*20

def developerData(request):
    if request.method=="POST" and 'submit' in request.POST:
        fm=DeveloperForm(request.POST)
        if fm.is_valid():
            print("It is valid part")
            p_rating=0
            b_rating=0
            q_rating=0
            t=fm.cleaned_data['projects']
            for x in t :
                p_rating=x.rating
            t=fm.cleaned_data['blogs']
            for x in t :
                b_rating=x.rating
            t=fm.cleaned_data['qa']
            for x in t :
                q_rating=x.rating
            print("rating ",p_rating,q_rating,b_rating)
            score=gen_score(q_rating,b_rating,p_rating)
            print("score by function",score)
            
            fm.cleaned_data['score']=score
            print(fm.cleaned_data)
            
            fm.save()
            messages.success(request,'Developer Added Successfully ..!')

    if request.method=='POST' and 'delete' in request.POST:
        id=request.POST['id']
        Developer.objects.get(pk=id).delete()
        messages.success(request , "Record deleted ..!")


    fm = DeveloperForm()
    devdata = Developer.objects.all()
    return render(request,'developer.html' , {'fm':fm , 'devdata':devdata})


def edit(request , id):
    instance  =  Developer.objects.get(pk=id)
    if request.method=="POST":
        fm=DeveloperForm(request.POST,instance=instance)

        if fm.is_valid:
            fm.save()
            return redirect('/adddev')
            messages.success(request,"UPDATED SUCCESSFULLY ..!!")
    fm=DeveloperForm(instance=instance)
    return render(request , 'edit.html' ,  context ={'fm':fm})

def search_view(request):
    form=SearchForm()
    if request.method=='POST':
        form=SearchForm(request.POST)
        if form.is_valid() :
            print("in the is_valid section ")
            location1=form.cleaned_data['location']
            tech=form.cleaned_data['technology']
            # id=request.POST['id']
            tech1 =Technology.objects.get(name=tech)
            print(tech1.name , tech1.id)
            # technology = list(tech1)
            result=Developer.objects.filter(location=location1 , technology = tech1.id)
            # result=Developer.objects.filter(location=location1,technology=4)
            return render(request,'data/searchresult.html',{'result':result})
    return render(request,'data/search.html',{'form':form})


