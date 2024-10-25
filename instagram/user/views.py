from django.shortcuts import render
from django.http import HttpResponse
from user import views
def indianuser(request,uid):
    user=[{'id':1,'name':'sameer','followers':20,'post':400,'started':'june2002'},
          {'id':2,'name':'syed','followers':220,'post':500,'started':'sept2020'},
          {'id':3,'name':'nithin','followers':670,'post':580,'started':'jun2017'}
          ]
    for item in user:
        if item.get('id')==uid:
            result=item
            if result is not None:
                return HttpResponse(f"<p>indianuser name:{result.get('name')}<br>user followers:{result.get('followers')}<br>user post:{result.get('post')}<br>started date:{result.get('started')}</p>")
            else:
                return HttpResponse("user not found")
    #return HttpResponse()
def ukuser(request,uid):
    user=[{'id':1,'name':'rock','followers':450,'post':100,'started':'june2010'},
          {'id':2,'name':'john','followers':750,'post':200,'started':'sept2015'},
          {'id':3,'name':'robert','followers':890,'post':117,'started':'feb2014'}
          ]
    for item in user:
        if item.get('id')==uid:
            result=item
            if result is not None:
                return HttpResponse(f"<p>ukuser name:{result.get('name')}<br>user followers:{result.get('followers')}<br>user post:{result.get('post')}<br>started date:{result.get('started')}</p>")
            else:
                return HttpResponse("user not found")
            
    #return HttpResponse()
def pakuser(request,uid):
    user=[{'id':1,'name':'adul','followers':4000000,'post':12,'started':'june2024'},
          {'id':2,'name':'razak','followers':123456,'post':14,'started':'sept2000'},
          {'id':3,'name':'karim','followers':986523,'post':16,'started':'feb2003'}
          ]
    for item in user:
        if item.get('id')==uid:
            result=item
            if result is not None:
                return HttpResponse(f"<p>pakuser name:{result.get('name')}<br>user followers:{result.get('followers')}<br>user post:{result.get('post')}<br>started date:{result.get('started')}</p>")
            else:
                return HttpResponse("user not found")
    #return HttpResponse()


# Create your views here.
