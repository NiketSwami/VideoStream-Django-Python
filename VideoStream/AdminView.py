from django.shortcuts import render
from . import pool

def AdminLogin(request):
    return render(request,"adminLogin.html",{"msg":""})


def CheckLogin(request):
 try:

   db,cmd= pool.connectionPooling()
   emailid= request.POST['emailid']
   password= request.POST['password']
   q="select * from adminlogin where emailid='{}'and password='{}'".format(emailid,password)
   cmd.execute(q)
   row=cmd.fetchone()
   if(row):
       return render(request,"Dashboard.html",{'row':row})
   else:
       return render(request,"AdminLogin.html",{'msg':'pls Input Valid EmailID/Password'})


 except Exception as e:
   print("errrrrrrr",e)
   return render(request, "AdminLogin.html",{'msg':"Server Error..."})
