from django.shortcuts import render

# Create your views here.
def func1(request):
    a=(request.POST.get('s1'))
    return render(request,'form.html',{'my':a})
def func2(request):
    result=None
    if request.method=="POST":
        a=int(request.POST.get('s1'))
        if a%2==0:
            result=True
        else:
            result=False
    return render(request,'even.html',{'res':result})
def func3(request):
    a=int(request.POST.get('s1'))
    b=int(request.POST.get('s2'))
    if a>b:
        result=a
    else:
        result=b
    return render(request,'twonum.html',{'res':result})
def func4(request):
    a=int(request.GET.get('s1'))
    count=0
    for i in range(2,a):
        if a%i==0:
             count+=1
    result=None
    if count==0:
        result=True
    else:
        result=False
    return render(request,'prime.html',{'res':result})
def func5(request):
    a=int(request.POST.get('s1'))
    org=a
    lis=[]
    sum=0
    while a>0:
        s=a%10
        a=a//10
        lis.append(s)
    l=len(lis)
    for i in lis:
        re=i**l
        sum=sum+re
    result=None
    if sum==org:
        result=True
    else:
        result=False
    return render(request,'amstr.html',{'res':result})
def func6(request):
    result=None
    d={'stu':[
        {'name':'sameer','Rollno':213389,'Totalsubjects':10,'passstubject':7,'failedsubject':3},
        {'name':'nithin','Rollno':213369,'Totalsubjects':10,'passstubject':10,'failedsubject':0},
        {'name':'syed','Rollno':213390,'Totalsubjects':10,'passstubject':4,'failedsubject':6},
        {'name':'sameer','Rollno':213388,'Totalsubjects':10,'passstubject':1,'failedsubject':9},
        ]
    }
    if request.method=="POST":
        a=int(request.POST.get('s1'))
        for i in d['stu']:
            if i['Rollno'] == a:
                result = i 
    print(result)
    return render(request,'stud.html',{'res':result})





''