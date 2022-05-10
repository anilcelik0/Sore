from django.urls import path
from pages import views

# http://127.0.0.1:8000/

urlpatterns = [
    path('',views.flow, name='flow'),
    path('2/',views.index2, name='index2'),
    path('flow2/',views.flow2, name='flow2'),
    path('reyting/',views.reyting, name='reyting'),
    path('search/',views.search, name='search'),
    path('<str:username>',views.profiles,name='profiles')

]

