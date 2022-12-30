from django.urls import path
from Home import views
urlpatterns = [
    path('',views.home, name = "home"),
    path('show/',views.show, name="show"),
    path('display/',views.display, name="display"),
    path('add/',views.add, name="add"),
    path('get_degrees/',views.get_degrees,name='get_degrees'),
    path('get_subjects/<int:id>',views.get_subjects, name="get_subjects"),
]