"""VideoStream URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import CategoryView
from . import ShowsView
from . import EpisodesView
from . import AdminView
from . import UserView

urlpatterns = [
    path('admin/', admin.site.urls),

    # UserInterface
    path('userview/',UserView.UserView),
    path('preview/', UserView.preview),
    path('tvpreview/', UserView.TVpreview),
    path('userdetailssubmit/', UserView.Userdetailssubmit),
    path('checkmobilenumber/', UserView.CheckMobileNumber),
    path('usersession/', UserView.UserSession),
    path('userlogout/', UserView.UserLogout),
    path('searching/',UserView.Searching),


    #Admin
    path('adminlogin/', AdminView.AdminLogin),
    path('checklogin', AdminView.CheckLogin),
    #category
    path('categoryinterface/', CategoryView.CategoryInterface),
    path('submitcategory', CategoryView.SubmitCategory),
    path('displayallcategory/', CategoryView.DisplayAll),
    path('categorybyid/', CategoryView.CategoryById),
    path('editdeletecategorydata/', CategoryView.EditDeleteCategoryData),
    path('editicon', CategoryView.Editicon),
    path('displayallcategoryjson/', CategoryView.DisplayAllJSON),
    #Shows
    path('showsinterface/', ShowsView.ShowsInterface),
    path('submitshow', ShowsView.SubmitShows),
    path('displayallshows/',ShowsView.DisplayAllShows),
    path('showsbyid/',ShowsView.ShowsById),
    path('editdeleteshowsdata/',ShowsView.EditDeleteShowsData),
    path('editposter',ShowsView.EditPoster),
    path('edittrailer',ShowsView.EditTrailer),
    path('editvideo',ShowsView.EditVideo),
    path('displayallshowsjson/', ShowsView.DisplayAllShowsJSON),
    #Episodes
    path('episodesinterface/',EpisodesView.EpisodesInterface),
    path('submitepisodes',EpisodesView.SubmitEpisodes),
    path('displayallepisodes/',EpisodesView.DisplayAllEpisodes),
    path('episodesbyid/',EpisodesView.EpisodesById),
    path('editdeleteepisodesdata/', EpisodesView.EditDeleteEpisodesData),
    path('editposterepisodes',EpisodesView.EditPosterEpisodes),
    path('edittrailerepisodes',EpisodesView.EditTrailerEpisodes),
    path('editvideoepisodes',EpisodesView.EditVideoEpisodes,)
]
