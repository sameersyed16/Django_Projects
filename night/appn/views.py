from django.shortcuts import render
d={'stuinfo':[
        {'name':'sameer','Rollno':'213389','Totalsubjects':10,'passstubject':7,'failedsubject':3},
        {'name':'nithin','Rollno':'213369','Totalsubjects':10,'passstubject':10,'failedsubject':0},
        {'name':'syed','Rollno':'213390','Totalsubjects':10,'passstubject':4,'failedsubject':6},
        {'name':'sameer','Rollno':'213388','Totalsubjects':10,'passstubject':1,'failedsubject':9},
                ]}
def res(request,Rollno):
    result=None
    for i in d.get('stuinfo'):
        if i.get('Rollno')==Rollno:
            result=i
            break
    if result is not None:
        return render(request,'posneg.html',result)
    else:
        return render(request,'posneg.html')
    
def sameer(request):
    return render(request,'index.html')
