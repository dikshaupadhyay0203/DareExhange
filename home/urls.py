from django.urls import path

from . import views
urlpatterns = [
   path("",views.home,name="home"),

   path("add-dare", views.create_dare, name="create_dare"),
   path("dares/",views.dares,name="dares"),
   path("delete_dare/<int:id>",views.delete_dare,name="delete_dare"),
   path("edit_dare/<int:id>",views.edit_dare,name="edit_dare"),
]



