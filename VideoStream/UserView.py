from django.shortcuts import render
from . import pool
from django.http import JsonResponse

def UserView(request):
    try:
        ses = ''
        user = ''

        try:
            if (request.session['USER']):
                ses = True
                user = request.session['USER']
            else:
                ses: False
                user = []
                print("USER", user)
            print("xxxxxxxxxxx", ses)

        except Exception as e:
            print("Session Error",e)




        db, cmd = pool.connectionPooling()
        q="select * from category"
        cmd.execute(q)
        rows=cmd.fetchall()

        q = "select * from shows where showstatus='Trending'"
        cmd.execute(q)
        trows = cmd.fetchall()

        q = "select * from shows where categoryid in (select categoryid from category where categoryname='TV Shows')"
        cmd.execute(q)
        tvrows = cmd.fetchall()

        db.close()
        return render(request, "userInterface.html",{'rows':rows,'trows':trows,'tvrows':tvrows,'ses':ses,'user':user})

    except Exception as e:
        return render(request, "userInterface.html",{'rows':[]})

def preview(request):
    ses = ''
    user = ''

    try:
        if (request.session['USER']):
            ses = True

            user = request.session['USER']
        else:
            ses: False
            user = []
        print("USER", user)

    except:
        pass

    row = request.GET['row']
    row = eval(row)
    #Main Menu
    db, cmd = pool.connectionPooling()
    q = "select * from category"
    cmd.execute(q)
    rows = cmd.fetchall()

    #Movies
    q = "select * from shows where categoryid=17"
    cmd.execute(q)
    movies = cmd.fetchall()

    db.close()
    return render(request, "Preview.html", {'row': row,'rows':rows,'movies':movies,'ses':ses,'user':user})

def TVpreview(request):
    try:
      row = request.GET['row']
      row = eval(row)

    # Main Menu
      db, cmd = pool.connectionPooling()
      q = "select * from category"
      cmd.execute(q)
      rows = cmd.fetchall()

    #Episodes
      q = "select * from episodes where categoryid=19 and showsid={}".format(row[0])
      cmd.execute(q)
      episodes = cmd.fetchall()


    # TVShows
      q = "select * from shows where categoryid=19"
      cmd.execute(q)
      tvshows = cmd.fetchall()

      db.close()
      return render(request, "TvPreview.html", {'row': row, 'episodes': episodes, 'tvshows': tvshows})
    except Exception as e:
        return render(request, "TvPreview.html",{'rows':[],'episodes':[]})

def Userdetailssubmit(request):
    try:
        db, cmd = pool.connectionPooling()
        mobileno = request.GET['mobileno']
        username = request.GET['username']
        age = request.GET['age']
        gender = request.GET['gender']
        status = request.GET['status']
        q = "insert into clientdetails (mobilenumber,username,age,gender,status) values('{0}','{1}','{2}','{3}','{4}')".format(mobileno,username,age,gender,status)

        print(q)

        cmd.execute(q)
        db.commit()
        db.close()
        return JsonResponse("Registration Completed Successfully", safe=False)

    except Exception as e:
        print("error:",e)
        return JsonResponse("Fail to Submit Record", safe=False)


def CheckMobileNumber(request):
    try:
        db, cmd = pool.connectionPooling()
        mobileno = request.GET['mobileno']

        q = "select * from clientdetails where mobilenumber='{}'".format(mobileno)

        print(q)
        cmd.execute(q)
        row = cmd.fetchone()
        db.close()
        return JsonResponse(row, safe=False)



    except Exception as e:
        print("error:",e)
        return JsonResponse("null", safe=False)

def UserSession(request):
    try:

        mobileno = request.GET['mobileno']
        username=request.GET['username']

        request.session["USER"]=[mobileno,username]
        print("Session Created",mobileno,username)
        return JsonResponse(True, safe=False)



    except Exception as e:
        print("error:",e)
        return JsonResponse(False, safe=False)


def UserLogout(request):
    try:
        del request.session['USER']
        return UserView(request)

    except Exception as e:
        print('error:',e)


def Searching(request):
    try:
        db, cmd = pool.connectionPooling()
        st = request.GET['st']

        q = "select * from shows where showname like '%{}%'".format(st)

        print(q)
        cmd.execute(q)
        rows = cmd.fetchall()
        db.close()
        return JsonResponse(rows, safe=False)



    except Exception as e:
        print("error:",e)
        return JsonResponse("null", safe=False)
