from django.shortcuts import render

# Create your views here.
def student(request):
    info={stuinfo:[{'name':'sameer','Rollno':213389,'Totalsubjects':10,'passstubject':7,'failedsubject':3},
                   {'name':'nithin','Rollno':213369,'Totalsubjects':10,'passstubject':10,'failedsubject':0},
                   {'name':'syed','Rollno':213390,'Totalsubjects':10,'passstubject':4,'failedsubject':6},
                   {'name':'sameer','Rollno':213388,'Totalsubjects':10,'passstubject':1,'failedsubject':9},
                   ]
                   }
    return render(request,'res.html')
def getinfo(request, num):
    result = None
    for i in info['stuinfo']:
        if i['Rollno'] == num:
            result = i
            break  
        if result is not None:
            d={'status':result}
            return render(request,'res.html',d)
        else:
            return render(request,'res.html',d)

