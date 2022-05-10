from rest_framework import status
from rest_framework import response
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  
from rest_framework.decorators import api_view, permission_classes
from rest_framework.serializers import Serializer
from rest_framework.views import APIView

from pages import models
from pages.api import serializers

#auth
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def restricted(request,*args, **kwargs):
    return Response(data="only for logged in user", status=status.HTTP_200_OK)

#photo
@api_view(['GET','POST'])
def photo_list_create_api_view(request):
    
    if request.method == 'GET':
        photos = models.Photo.objects.all()
        serializer = serializers.PhotoSerializers(photos, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = serializers.PhotoSerializers(data=request.data, files=request.FILES)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST) 


@api_view(['GET','PUT','DELETE'])
def photo_detail_api_view(request,id):
    try:
        photo_instance = models.Photo.objects.get(id=id)
    
    except models.Photo.DoesNotExist:
        return Response(
            {
                'errors':404,
                'message':f'böyle bir fotoğraf bulunamadı'
            },
            status=status.status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = serializers.PhotoSerializers(photo_instance)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = serializers.PhotoSerializers(photo_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE':
        photo_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#photo2
@api_view(['GET','POST'])
def photo2_list_create_api_view(request):
    
    if request.method == 'GET':
        photos = models.Photo2.objects.all()
        serializer = serializers.Photo2Serializers(photos, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = serializers.Photo2Serializers(data=request.data, files=request.FILES)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST) 


@api_view(['GET','PUT','DELETE'])
def photo2_detail_api_view(request,id):
    try:
        photo2_instance = models.Photo2.objects.get(id=id)
    
    except models.Photo2.DoesNotExist:
        return Response(
            {
                'errors':404,
                'message':f'böyle bir fotoğraf bulunamadı'
            },
            status=status.status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = serializers.Photo2Serializers(photo2_instance)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = serializers.Photo2Serializers(photo2_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE':
        photo2_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#ppUser
@api_view(['GET','POST'])
def ppUser_list_create_api_view(request):
    
    if request.method == 'GET':
        photos = models.ppUser.objects.all()
        serializer = serializers.ppUserSerializers(photos, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = serializers.ppUserSerializers(data=request.data, files=request.FILES)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST) 


@api_view(['GET','PUT','DELETE'])
def ppUser_detail_api_view(request,id):
    try:
        ppUser_instance = models.ppUser.objects.get(id=id)
    
    except models.ppUser.DoesNotExist:
        return Response(
            {
                'errors':404,
                'message':f'böyle bir fotoğraf bulunamadı'
            },
            status=status.status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = serializers.ppUserSerializers(ppUser_instance)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = serializers.ppUserSerializers(ppUser_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE':
        ppUser_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#followEvent
@api_view(['GET','POST'])
def followEvent_list_create_api_view(request):
    
    if request.method == 'GET':
        photos = models.followEvent.objects.all()
        serializer = serializers.followEventSerializers(photos, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = serializers.followEventSerializers(data=request.data, files=request.FILES)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST) 


@api_view(['GET','PUT','DELETE'])
def followEvent_detail_api_view(request,id):
    try:
        followEvent_instance = models.followEvent.objects.get(id=id)
    
    except models.followEvent.DoesNotExist:
        return Response(
            {
                'errors':404,
                'message':f'böyle bir fotoğraf bulunamadı'
            },
            status=status.status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = serializers.followEventSerializers(followEvent_instance)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = serializers.followEventSerializers(followEvent_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE':
        followEvent_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#viewing2
@api_view(['GET','POST'])
def viewing2_list_create_api_view(request):
    
    if request.method == 'GET':
        photos = models.viewing2.objects.all()
        serializer = serializers.viewing2Serializers(photos, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = serializers.viewing2Serializers(data=request.data, files=request.FILES)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST) 


@api_view(['GET','PUT','DELETE'])
def viewing2_detail_api_view(request,id):
    try:
        viewing2_instance = models.viewing2.objects.get(id=id)
    
    except models.viewing2.DoesNotExist:
        return Response(
            {
                'errors':404,
                'message':f'böyle bir fotoğraf bulunamadı'
            },
            status=status.status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = serializers.viewing2Serializers(viewing2_instance)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = serializers.viewing2Serializers(viewing2_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE':
        viewing2_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#feedback
@api_view(['GET','POST'])
def feedback_list_create_api_view(request):
    
    if request.method == 'GET':
        photos = models.feedback.objects.all()
        serializer = serializers.feedbackSerializers(photos, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = serializers.feedbackSerializers(data=request.data, files=request.FILES)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST) 


@api_view(['GET','PUT','DELETE'])
def feedback_detail_api_view(request,id):
    try:
        feedback_instance = models.feedback.objects.get(id=id)
    
    except models.feedback.DoesNotExist:
        return Response(
            {
                'errors':404,
                'message':f'böyle bir fotoğraf bulunamadı'
            },
            status=status.status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = serializers.feedbackSerializers(feedback_instance)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = serializers.feedbackSerializers(feedback_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE':
        feedback_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#photoLiked
@api_view(['GET','POST'])
def photoLiked_list_create_api_view(request):
    
    if request.method == 'GET':
        photos = models.photoLiked.objects.all()
        serializer = serializers.photoLikedSerializers(photos, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = serializers.photoLikedSerializers(data=request.data, files=request.FILES)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST) 


@api_view(['GET','PUT','DELETE'])
def photoLiked_detail_api_view(request,id):
    try:
        photoLiked_instance = models.photoLiked.objects.get(id=id)
    
    except models.photoLiked.DoesNotExist:
        return Response(
            {
                'errors':404,
                'message':f'böyle bir fotoğraf bulunamadı'
            },
            status=status.status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = serializers.photoLikedSerializers(photoLiked_instance)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = serializers.photoLikedSerializers(photoLiked_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE':
        photoLiked_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#photoLiked2
@api_view(['GET','POST'])
def photoLiked2_list_create_api_view(request):
    
    if request.method == 'GET':
        photos = models.photoLiked2.objects.all()
        serializer = serializers.photoLiked2Serializers(photos, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = serializers.photoLiked2Serializers(data=request.data, files=request.FILES)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST) 


@api_view(['GET','PUT','DELETE'])
def photoLiked2_detail_api_view(request,id):
    try:
        photoLiked2_instance = models.photoLiked2.objects.get(id=id)
    
    except models.photoLiked2.DoesNotExist:
        return Response(
            {
                'errors':404,
                'message':f'böyle bir fotoğraf bulunamadı'
            },
            status=status.status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = serializers.photoLiked2Serializers(photoLiked2_instance)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = serializers.photoLiked2Serializers(photoLiked2_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE':
        photoLiked2_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#photoBlock
@api_view(['GET','POST'])
def photoBlock_list_create_api_view(request):
    
    if request.method == 'GET':
        photos = models.photoBlock.objects.all()
        serializer = serializers.photoBlockSerializers(photos, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = serializers.photoBlockSerializers(data=request.data, files=request.FILES)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST) 


@api_view(['GET','PUT','DELETE'])
def photoBlock_detail_api_view(request,id):
    try:
       photoBlock_instance = models.photoBlock.objects.get(id=id)
    
    except models.photoBlock.DoesNotExist:
        return Response(
            {
                'errors':404,
                'message':f'böyle bir fotoğraf bulunamadı'
            },
            status=status.status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = serializers.photoBlockSerializers(photoBlock_instance)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = serializers.photoBlockSerializers(photoBlock_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE':
        photoBlock_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#photoBlock2
@api_view(['GET','POST'])
def photoBlock2_list_create_api_view(request):
    
    if request.method == 'GET':
        photos = models.photoBlock2.objects.all()
        serializer = serializers.photoBlock2Serializers(photos, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = serializers.photoBlock2Serializers(data=request.data, files=request.FILES)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST) 


@api_view(['GET','PUT','DELETE'])
def photoBlock2_detail_api_view(request,id):
    try:
       photoBlock2_instance = models.photoBlock2.objects.get(id=id)
    
    except models.photoBlock2.DoesNotExist:
        return Response(
            {
                'errors':404,
                'message':f'böyle bir fotoğraf bulunamadı'
            },
            status=status.status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = serializers.photoBlock2Serializers(photoBlock2_instance)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = serializers.photoBlock2Serializers(photoBlock2_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE':
        photoBlock2_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#photoSave
@api_view(['GET','POST'])
def photoSave_list_create_api_view(request):
    
    if request.method == 'GET':
        photos = models.photoSave.objects.all()
        serializer = serializers.photoSaveSerializers(photos, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = serializers.photoSaveSerializers(data=request.data, files=request.FILES)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST) 


@api_view(['GET','PUT','DELETE'])
def photoSave_detail_api_view(request,id):
    try:
       photoSave_instance = models.photoSave.objects.get(id=id)
    
    except models.photoSave.DoesNotExist:
        return Response(
            {
                'errors':404,
                'message':f'böyle bir fotoğraf bulunamadı'
            },
            status=status.status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = serializers.photoSaveSerializers(photoSave_instance)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = serializers.photoSaveSerializers(photoSave_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE':
        photoSave_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
