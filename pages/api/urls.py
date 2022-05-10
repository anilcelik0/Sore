from django.urls import path, include
from pages.api import views as api_views


urlpatterns = [
    path('photo/',api_views.photo_list_create_api_view, name='photos-list'),
    path('photo/<int:id>',api_views.photo_detail_api_view, name='photo-detay'),

    path('photo2/',api_views.photo2_list_create_api_view, name='photos2-list'),
    path('photo2/<int:id>',api_views.photo2_detail_api_view, name='photo2-detay'),
    
    path('ppUser/',api_views.ppUser_list_create_api_view, name='ppUser-list'),
    path('ppUser/<int:id>',api_views.ppUser_detail_api_view, name='ppUser-detay'),
   
    path('followEvent/',api_views.followEvent_list_create_api_view, name='followEvent-list'),
    path('followEvent/<int:id>',api_views.followEvent_detail_api_view, name='followEvent-detay'),
   
    path('viewing2/',api_views.viewing2_list_create_api_view, name='viewing2-list'),
    path('viewing2/<int:id>',api_views.viewing2_detail_api_view, name='viewing2-detay'),
   
    path('feedback/',api_views.feedback_list_create_api_view, name='feedback-list'),
    path('feedback/<int:id>',api_views.feedback_detail_api_view, name='feedback-detay'),
   
    path('photoLiked/',api_views.photoLiked_list_create_api_view, name='photoLiked-list'),
    path('photoLiked/<int:id>',api_views.photoLiked_detail_api_view, name='photoLiked-detay'),
   
    path('photoLiked2/',api_views.photoLiked2_list_create_api_view, name='photoLiked2-list'),
    path('photoLiked2/<int:id>',api_views.photoLiked2_detail_api_view, name='photoLiked2-detay'),
   
    path('photoBlock/',api_views.photoBlock_list_create_api_view, name='photoBlock-list'),
    path('photoBlock/<int:id>',api_views.photoBlock_detail_api_view, name='photoBlock-detay'),
   
    path('photoBlock2/',api_views.photoBlock2_list_create_api_view, name='photoBlock2-list'),
    path('photoBlock2/<int:id>',api_views.photoBlock2_detail_api_view, name='photoBlock2-detay'),
   
    path('photoSave/',api_views.photoSave_list_create_api_view, name='photoSave-list'),
    path('photoSave/<int:id>',api_views.photoSave_detail_api_view, name='photoSave-detay'),


    path('',include('djoser.urls')),
    path('',include('djoser.urls.authtoken')),
    path('restriced/',api_views.restricted),

]
