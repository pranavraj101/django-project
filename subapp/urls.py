from django.contrib import admin
from django.urls import path,include
from subapp import views


app_name = "subapp"

urlpatterns = [
    path('home/',views.home,name="home"),
    path('hi/<name>',views.hiname,name="hi"),
    path('add<a>+<b>',views.add,name="add"),
    path('temp/',views.temp_Demo,name="demo"),
    path('ghat/',views.ghat,name="ghat"),
    path('rmg/',views.rmg,name="rmg"),
    path('sarnath/',views.sarnath,name="sarnath"),
    path('temple/',views.temple,name="temple"),
    path('varansi_tourism/',views.varanasi_tour,name="varansi_tour"),
    path('hometemp/',views.hometemp,name="hometemp"),
    path('aboutus/',views.aboutus,name="aboutus"),
    path('form/',views.form,name="form")
    

]
