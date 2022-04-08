from django.shortcuts import render
from . import pool
from django.views.decorators.clickjacking import xframe_options_exempt
import os
@xframe_options_exempt
def EpisodesInterface(request):
    return render(request,"EpisodesInterface.html")

@xframe_options_exempt
def SubmitEpisodes(request):
 try:

   db,cmd= pool.connectionPooling()
   categoryid= request.POST['categoryid']
   showsid=request.POST['showsid']
   episodenumber = request.POST['episodenumber']
   description= request.POST['description']
   poster= request.FILES['poster']
   trailer= request.FILES['trailer']
   video= request.FILES['video']


   q="insert into episodes(categoryid,showsid,episodenumber,description,poster,trailer,video)values('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(categoryid,showsid,episodenumber,description,poster.name,trailer.name,video.name)
   print(q)
   cmd.execute(q)
   db.commit()
   #wb(write bytes)
   F=open("D:/VideoStream/assets/"+poster.name,"wb")
   for chunk in poster.chunks():
       F.write(chunk)
   F.close()

   F = open("D:/VideoStream/assets/"+trailer.name, "wb")
   for chunk in trailer.chunks():
       F.write(chunk)
   F.close()

   F = open("D:/VideoStream/assets/"+video.name, "wb")
   for chunk in video.chunks():
       F.write(chunk)
   F.close()

   db.close()
   return render(request, "EpisodesInterface.html",{'status':True})

 except Exception as e:
   print("errrrrrrr",e)
   return render(request, "EpisodesInterface.html",{'status':False})


@xframe_options_exempt
def DisplayAllEpisodes(request):
    try:
        db, cmd = pool.connectionPooling()
        #q="select * from episodes"
        q = "select E.*,(select C.categoryname from category C where C.categoryid=E.categoryid)  from episodes E"
        print(q)
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()
        return render(request,"DisplayAllEpisodes.html",{'rows':rows})

    except Exception as e:
        print(e)
        return render(request,"DisplayAllEpisodes.html",{'rows':[]})

@xframe_options_exempt
def EpisodesById(request):
    try:
        eid=request.GET['eid']
        db, cmd = pool.connectionPooling()
        #q="select * from episodes where episodeid={}".format(eid)
        q = "select E.*,(select C.categoryname from category C where C.categoryid=E.categoryid)  from episodes E where E.episodeid={}".format(eid)

        cmd.execute(q)
        row=cmd.fetchone()
        db.close()
        return render(request,"EpisodesById.html",{'row':row})

    except Exception as e:
        return render(request,"EpisodesById.html",{'row':[]})

@xframe_options_exempt
def EditDeleteEpisodesData(request):
    try:
        btn = request.GET["btn"]
        if (btn == "Edit"):
            episodeid = request.GET['episodeid']
            categoryid = request.GET['categoryid']
            showsid = request.GET['showsid']
            episodenumber = request.GET['episodenumber']
            description = request.GET['description']

            db, cmd = pool.connectionPooling()
            q = "update episodes set categoryid='{}',showsid= '{}',episodenumber='{}', description='{}' where episodeid={}".format(
                categoryid, showsid,episodenumber, description, episodeid)
            print(q)
            cmd.execute(q)
            db.commit()
            db.close()

        elif (btn == "Delete"):

            db, cmd = pool.connectionPooling()
            episodeid = request.GET['episodeid']
            q = "delete from episodes  where episodeid={}".format(episodeid)
            cmd.execute(q)
            db.commit()
            db.close()

        return render(request, "EpisodesById.html", {'status': True})

    except Exception as e:
        print(e)
        return render(request, "EpisodesById.html", {'status': False})

@xframe_options_exempt
def EditPosterEpisodes(request):
 try:

   db,cmd= pool.connectionPooling()

   episodeid= request.POST['episodeid']
   filename = request.POST['filename']
   poster= request.FILES['poster']
   q="update episodes set poster='{0}' where episodeid={1}".format(poster.name,episodeid)
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
   return render(request, "EpisodesInterface.html",{'status':True})

 except Exception as e:
   print("errrrrrrr",e)
   return render(request, "EpisodesInterface.html",{'status':False})

@xframe_options_exempt
def EditTrailerEpisodes(request):
 try:

   db,cmd= pool.connectionPooling()

   episodeid= request.POST['episodeid']
   filename = request.POST['filename']
   trailer= request.FILES['trailer']
   q="update episodes set trailer='{0}' where episodeid={1}".format(trailer.name,episodeid)
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
   return render(request, "EpisodesInterface.html",{'status':True})

 except Exception as e:
   print("errrrrrrr",e)
   return render(request, "EpisodesInterface.html",{'status':False})

@xframe_options_exempt
def EditVideoEpisodes(request):
 try:

   db,cmd= pool.connectionPooling()

   episodeid= request.POST['episodeid']
   filename = request.POST['filename']
   video= request.FILES['video']
   q="update episodes set video='{0}' where episodeid={1}".format(video.name,episodeid)
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
   return render(request, "EpisodesInterface.html",{'status':True})

 except Exception as e:
   print("errrrrrrr",e)
   return render(request, "EpisodesInterface.html",{'status':False})






