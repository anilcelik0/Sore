from django.urls import path
from user import views

# http://127.0.0.1:8000/

urlpatterns = [
    path('alogout/', views.logout, name= 'alogout'),
    path('alogin/', views.login, name= 'alogin'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name = 'profile'),
    path('upload/', views.uploadimage, name = 'upload'),
    path('save/', views.saveimage, name = 'save'),
    path('settings/', views.settings, name = 'settings'),
]