from django.shortcuts import render
from . import pool
import os
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import JsonResponse

@xframe_options_exempt
def ShowsInterface(request):
    return render(request, "ShowsInterface.html")

@xframe_options_exempt
def SubmitShows(request):
    try:
        db, cmd = pool.connectionPooling()
        categoryid = request.POST['categoryid']
        showname = request.POST['showname']
        description = request.POST['description']
        showtype = request.POST['showtype']
        year = request.POST['year']
        rating = request.POST['rating']
        artist = request.POST['artist']
        status = request.POST['status']
        episodes = request.POST['episodes']
        showstatus = request.POST['showstatus']
        poster = request.FILES['poster']
        trailer = request.FILES['trailer']
        video = request.FILES['video']

        q ="insert into shows(categoryid,showname,description,showtype,year,rating,artist,status,episodes,showstatus,poster,trailer,video)values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}')".format(categoryid,showname,description,showtype,year,rating,artist,status,episodes,showstatus,poster.name,trailer.name,video.name)

        print(q)
        cmd.execute(q)
        db.commit()
        # wb(write bytes)
        F = open("D:/VideoStream/assets/" + poster.name, "wb")
        for chunk in poster.chunks():
           F.write(chunk)
        F.close()

        G= open("D:/VideoStream/assets/" + trailer.name, "wb")
        for chunk in trailer.chunks():
            G.write(chunk)
        G.close()

        H = open("D:/VideoStream/assets/" + video.name, "wb")
        for chunk in video.chunks():
            H.write(chunk)
        H.close()
        db.close()
        return render(request, "ShowsInterface.html", {'status': True})

    except Exception as e:
      print("errrrrrrr", e)
      return render(request, "ShowsInterface.html", {'status': False})

@xframe_options_exempt
def DisplayAllShows(request):
    try:
        db, cmd = pool.connectionPooling()
        #q="select * from shows"
        q = "select S.*,(select C.categoryname from category C where C.categoryid=S.categoryid)  from shows S"
        print(q)
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()
        return render(request,"DisplayAllShows.html",{'rows':rows})

    except Exception as e:
        return render(request,"DisplayAllShows.html",{'rows':[]})

@xframe_options_exempt
def ShowsById(request):
    try:
        sid=request.GET['sid']
        db, cmd = pool.connectionPooling()
        #q="select * from shows where showsid={}".format(sid)
        q="select S.*,(select C.categoryname from category C where C.categoryid=S.categoryid)  from shows S where S.showsid={}".format(sid)

        print(q)
        cmd.execute(q)
        row=cmd.fetchone()
        db.close()
        return render(request,"ShowsById.html",{'row':row})

    except Exception as e:
        print(e)
        return render(request,"ShowsById.html",{'row':[]})

@xframe_options_exempt
def EditDeleteShowsData(request):
    try:
      btn=request.GET["btn"]
      if(btn=="Edit"):
          showsid=request.GET['showsid']
          categoryid = request.GET['categoryid']
          showname = request.GET['showname']
          description = request.GET['description']
          showtype = request.GET['showtype']
          year = request.GET['year']
          rating = request.GET['rating']
          artist = request.GET['artist']
          status = request.GET['status']
          episodes = request.GET['episodes']
          showstatus = request.GET['showstatus']


          db, cmd = pool.connectionPooling()
          q="update shows set categoryid='{}',showname='{}', description='{}',showtype='{}',year='{}',rating='{}',artist='{}',status='{}',episodes='{}',showstatus='{}' where showsid={}" .format(categoryid,showname,description,showtype,year,rating,artist,status,episodes,showstatus,showsid)
          print(q)
          cmd.execute(q)
          db.commit()
          db.close()

      elif(btn=="Delete"):

          db, cmd = pool.connectionPooling()
          showsid=request.GET['showsid']
          q = "delete from shows  where showsid={}".format(showsid)
          cmd.execute(q)
          db.commit()
          db.close()

      return render(request,"ShowsById.html",{'status':True})

    except Exception as e:
        print(e)
        return render(request,"ShowsById.html",{'status':False})


@xframe_options_exempt
def EditPoster(request):
 try:

   db,cmd= pool.connectionPooling()

   showsid= request.POST['showsid']
   filename = request.POST['filename']
   poster= request.FILES['poster']
   q="update shows set poster='{0}' where showsid={1}".format(poster.name,showsid)
   print(q)
   cmd.execute(q)
   db.commit()
   #wb(write bytes)
   F=open("D:/VideoStream/assets/"+poster.name,"wb")
   for chunk in poster.chunks():
       F.write(chunk)
   F.close()
   os.remove("D:/VideoStream/assets/"+filename)
   db.close()
   return render(request, "ShowsInterface.html",{'status':True})

 except Exception as e:
   print("errrrrrrr",e)
   return render(request, "ShowsInterface.html",{'status':False})

@xframe_options_exempt
def EditTrailer(request):
 try:

   db,cmd= pool.connectionPooling()

   showsid= request.POST['showsid']
   filename = request.POST['filename']
   trailer= request.FILES['trailer']
   q="update shows set trailer='{0}' where showsid={1}".format(trailer.name,showsid)
   print(q)
   cmd.execute(q)
   db.commit()
   #wb(write bytes)
   F=open("D:/VideoStream/assets/"+trailer.name,"wb")
   for chunk in trailer.chunks():
       F.write(chunk)
   F.close()
   os.remove("D:/VideoStream/assets/"+filename)
   db.close()
   return render(request, "ShowsInterface.html",{'status':True})

 except Exception as e:
   print("errrrrrrr",e)
   return render(request, "ShowsInterface.html",{'status':False})


@xframe_options_exempt
def EditVideo(request):
 try:

   db,cmd= pool.connectionPooling()

   showsid= request.POST['showsid']
   filename = request.POST['filename']
   video= request.FILES['video']
   q="update shows set video='{0}' where showsid={1}".format(video.name,showsid)
   print(q)
   cmd.execute(q)
   db.commit()
   #wb(write bytes)
   F=open("D:/VideoStream/assets/"+video.name,"wb")
   for chunk in video.chunks():
       F.write(chunk)
   F.close()
   os.remove("D:/VideoStream/assets/"+filename)
   db.close()
   return render(request, "ShowsInterface.html",{'status':True})

 except Exception as e:
   print("errrrrrrr",e)
   return render(request, "ShowsInterface.html",{'status':False})

@xframe_options_exempt
def DisplayAllShowsJSON(request):
    try:
        cid=request.GET["cid"]
        db, cmd = pool.connectionPooling()
        q="select * from shows"
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()
        return JsonResponse(rows, safe=False)
    except Exception as e:
        print(e)
        return JsonResponse([], safe=False)


