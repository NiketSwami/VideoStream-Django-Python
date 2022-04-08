from django.shortcuts import render
from . import pool
import os
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import JsonResponse

@xframe_options_exempt
def CategoryInterface(request):
    return render(request,"CategoryInterface.html")

@xframe_options_exempt
def SubmitCategory(request):
 try:

   db,cmd= pool.connectionPooling()
   categoryname= request.POST['categoryname']
   description= request.POST['description']
   icon= request.FILES['icon']
   q="insert into category(categoryname,description,icon)values('{0}','{1}','{2}')".format(categoryname,description,icon.name)
   print(q)
   cmd.execute(q)
   db.commit()
   #wb(write bytes)
   F=open("D:/VideoStream/assets/"+icon.name,"wb")
   for chunk in icon.chunks():
       F.write(chunk)
   F.close()
   db.close()
   return render(request, "CategoryInterface.html",{'status':True})

 except Exception as e:
   print("errrrrrrr",e)
   return render(request, "CategoryInterface.html",{'status':False})

@xframe_options_exempt
def DisplayAll(request):
    try:
        db, cmd = pool.connectionPooling()
        q="select * from category"
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()
        return render(request,"DisplayAllCategories.html",{'rows':rows})

    except Exception as e:
        return render(request,"DisplayAllCategories.html",{'rows':[]})

@xframe_options_exempt
def CategoryById(request):
    try:
        cid=request.GET['cid']
        db, cmd = pool.connectionPooling()
        q="select * from category where categoryid={}".format(cid)
        cmd.execute(q)
        row=cmd.fetchone()
        db.close()
        return render(request,"CategoryById.html",{'row':row})

    except Exception as e:
        return render(request,"CategoryById.html",{'row':[]})

@xframe_options_exempt
def EditDeleteCategoryData(request):
    try:
      btn=request.GET["btn"]
      if(btn=="Edit"):
          categoryid=request.GET['categoryid']
          categoryname=request.GET['categoryname']
          description=request.GET['description']


          db, cmd = pool.connectionPooling()
          q="update category set categoryname='{}', description='{}' where categoryid={}".format(categoryname,description,categoryid)
          cmd.execute(q)
          db.commit()
          db.close()

      elif(btn=="Delete"):

          db, cmd = pool.connectionPooling()
          categoryid=request.GET['categoryid']
          q = "delete from category  where categoryid={}".format(categoryid)
          cmd.execute(q)
          db.commit()
          db.close()

      return render(request,"CategoryById.html",{'status':True})

    except Exception as e:
        print(e)
        return render(request,"CategoryById.html",{'status':False})

@xframe_options_exempt
def Editicon(request):
 try:

   db,cmd= pool.connectionPooling()

   categoryid= request.POST['categoryid']
   filename = request.POST['filename']
   icon= request.FILES['icon']
   q="update category set icon='{0}' where categoryid={1}".format(icon.name,categoryid)
   print(q)
   cmd.execute(q)
   db.commit()
   #wb(write bytes)
   F=open("D:/VideoStream/assets/"+icon.name,"wb")
   for chunk in icon.chunks():
       F.write(chunk)
   F.close()
   os.remove("D:/VideoStream/assets/"+filename)
   db.close()
   return render(request, "CategoryInterface.html",{'status':True})

 except Exception as e:
   print("errrrrrrr",e)
   return render(request, "CategoryInterface.html",{'status':False})


@xframe_options_exempt
def DisplayAllJSON(request):
    try:
        db, cmd = pool.connectionPooling()
        q="select * from category"
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()
        return JsonResponse(rows, safe=False)
    except Exception as e:
        print(e)
        return JsonResponse([], safe=False)


