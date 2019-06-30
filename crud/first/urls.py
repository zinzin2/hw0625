from django.urls import path
from . import views
urlpatterns=[
    path('one/',views.one,name="one"),
    path('two/',views.two,name="two"),
    path('main/',views.main,name="main"),
    path('myprofile/',views.myprofile,name="myprofile"),
    path('edit/',views.edit,name="edit"),
]