from typing import ContextManager
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from pages.models import Photo, Photo2, ppUser, followEvent, viewing2,feedback,photoLiked,photoBlock2,photoBlock,photoLiked2,photoSave
from django.contrib.auth.models import User
import random
from django.contrib import auth
from django.contrib import messages
from django.db.models import Q
import datetime
from user.views import login


# Create your views here.

def index2(request):      
    if request.user.is_authenticated:
        if viewing2.objects.filter(following = request.user,view=0).exists():
            if request.method == "POST":
                if 'btn1' in request.POST:
                    resim1 = request.POST['resim1']
                    resim1 = resim1[12:]
                    resim2 = request.POST['resim2']
                    resim2 = resim2[12:]
                    if photoLiked2.objects.filter(photo_name1 = resim1, photo_name2 = resim2 ,username =request.user.username).exists() == False:
                        photoLiked2.objects.create(username=request.user.username, photo_name1=resim1, photo_name2 = resim2).save()

                    resim = Photo2.objects.get(photo_name1 = resim1,photo_name2 = resim2)
                    resim.reyting +=1
                    resim.shows +=1
                    resim.save()
                    viewing2.objects.filter(photo_name=resim1,following=request.user).update(view=1)
                        
                    if viewing2.objects.filter(following = request.user,view=0).exists():
                        rand = random.choice(viewing2.objects.filter(following = request.user,view=0))

                        rand = Photo2.objects.get(photo_name1=rand.photo_name,photo_name2=rand.photo_name2,username = rand.followed)
                        if rand.reyting +rand.reyting2 == 0:
                            rey1=50
                            rey2=50
                        else:
                            rey1 = int(rand.reyting *100 / (rand.reyting+rand.reyting2))
                            rey2 = int(rand.reyting2 *100 / (rand.reyting+rand.reyting2))
                            if rey1+rey2 ==99:
                                rey1+=1

                        link = 'pages/image/'+rand.photo_name1.name
                        link2 = 'pages/image/'+rand.photo_name2.name
                        user = request.user

                        res = ppUser.objects.filter(username = user.username).first()
                        context = {
                            'fotos':link,
                            'kullanici':rand.username,
                            'reyting':rand.reyting,
                            'fotos2':link2,
                            'reyting2':rand.reyting2,
                            'res':res,
                            'rey1':rey1,
                            'rey2':rey2,
                        }

                        return render(request, 'pages/index2.html',context) 
                                
                    else:
                        messages.add_message(request,messages.SUCCESS,"Görülmemiş gönderi yok global'e yönlendirildiniz..")
                        return redirect('flow2')


                elif 'btn2' in request.POST:
                    resim1 = request.POST['resim1']
                    resim1 = resim1[12:]
                    resim2 = request.POST['resim2']
                    resim2 = resim2[12:]
                    if photoLiked2.objects.filter(photo_name1 = resim1, photo_name2 = resim2 ,username =request.user.username).exists() == False:
                        photoLiked2.objects.create(username=request.user.username, photo_name1=resim1, photo_name2 = resim2).save()

                    resim = Photo2.objects.get(photo_name1 = resim1,photo_name2 = resim2)
                    resim.reyting2 +=1
                    resim.shows += 1
                    resim.save()

                    viewing2.objects.filter(photo_name2=resim2,following=request.user).update(view=1)

                    if viewing2.objects.filter(following = request.user,view=0).exists():
                        rand = random.choice(viewing2.objects.filter(following = request.user,view=0))

                        link = 'pages/image/'+rand.photo_name
                        link2 = 'pages/image/'+rand.photo_name2
                        user = request.user

                        rand = Photo2.objects.get(photo_name1=rand.photo_name,photo_name2=rand.photo_name2,username = rand.followed)
                        if rand.reyting +rand.reyting2 == 0:
                            rey1=50
                            rey2=50
                        else:
                            rey1 = int(rand.reyting *100 / (rand.reyting+rand.reyting2))
                            rey2 = int(rand.reyting2 *100 / (rand.reyting+rand.reyting2))
                            if rey1+rey2 ==99:
                                rey1+=1
                        
                        res = ppUser.objects.filter(username = user.username).first()
                        context = {
                            'fotos':link,
                            'kullanici':rand.username,
                            'reyting':rand.reyting,
                            'fotos2':link2,
                            'reyting2':rand.reyting2,
                            'res':res,
                            'rey1':rey1,
                            'rey2':rey2,
                        }

                        return render(request, 'pages/index2.html',context)   

                    else:
                        messages.add_message(request,messages.SUCCESS,"Görülmemiş gönderi yok global'e yönlendirildiniz..")
                        return redirect('flow2')
                else:

                    if 'bildir' in request.POST:
                        resim1 = request.POST['resim1']
                        resim1 = resim1[12:]
                        resim2 = request.POST['resim2']
                        resim2 = resim2[12:]                    
                        resim = Photo2.objects.get(photo_name1 = resim1,photo_name2 = resim2)

                        feedback.objects.create(complaining = request.user.username,complained= resim.username,photo_name = resim1,photo_name2 = resim2).save()
                        messages.add_message(request,messages.SUCCESS,"Resim incelenmek üzere listeye alınmıştır. Teşekkürler..")
                        return redirect('index2')

                    elif 'dnsee' in request.POST:
                        resim1 = request.POST['resim1']
                        resim1 = resim1[12:]
                        resim2 = request.POST['resim2']
                        resim2 = resim2[12:]
                        photoBlock2.objects.create(username = request.user.username,photo_name1 = resim1,photo_name2 = resim2).save()
                        messages.add_message(request,messages.SUCCESS,"Resim bir daha gösterilmeyecektir.")
                        return redirect('flow2')

                    else:
                        return redirect('index2')

            else:
                rand = random.choice(viewing2.objects.filter(following = request.user,view=0))

                link = 'pages/image/'+rand.photo_name
                link2 = 'pages/image/'+rand.photo_name2
                user = request.user

                rand = Photo2.objects.get(photo_name1=rand.photo_name,photo_name2=rand.photo_name2,username = rand.followed)
                if rand.reyting +rand.reyting2 == 0:
                    rey1=50
                    rey2=50
                else:
                    rey1 = int(rand.reyting *100 / (rand.reyting+rand.reyting2))
                    rey2 = int(rand.reyting2 *100 / (rand.reyting+rand.reyting2))
                    if rey1+rey2 ==99:
                        rey1+=1

                res = ppUser.objects.filter(username = user.username).first()
                context = {
                    'fotos':link,
                    'kullanici':rand.username,
                    'reyting':rand.reyting,
                    'fotos2':link2,
                    'reyting2':rand.reyting2,
                    'res':res,
                    'rey1':rey1,
                    'rey2':rey2,
                }

                return render(request, 'pages/index2.html',context) 
        else:
            messages.add_message(request,messages.SUCCESS,"Görülmemiş gönderi yok global'e yönlendirildiniz..")
            return redirect('flow2')
                
    else:
        return HttpResponse('<h2>giriş yapmalısınız<h2>')


def flow(request):
    if request.method == "POST":
    
        if 'btn1' in request.POST:
            resim1 = request.POST['resim1']
            resim1 = resim1[12:]
            if request.user.is_authenticated and photoLiked.objects.filter(photo_name = resim1 ,username =request.user.username).exists() == False:
                photoLiked.objects.create(username=request.user.username, photo_name=resim1).save()
            a = request.POST['a']
            a = int(a) + 1
            b = 0

            if a == 5:
                a = 0
                rand1 = random.choice(Photo.objects.all())
                rand1.shows +=1
                rand1.performance = int(rand1.reyting/rand1.shows*100)
                rand1.save()

                    
                rand2 = random.choice(Photo.objects.filter(Q(performance__lte=rand1.performance+20)&Q(performance__gt=rand1.performance-20)&~Q(photo_name=rand1.photo_name)))
                rand2.shows +=1
                rand2.performance = int(rand2.reyting/rand2.shows*100)
                rand2.save()

                link = 'pages/image/'+rand1.photo_name.name
                link2 = 'pages/image/'+rand2.photo_name.name
                user = request.user
                res = ppUser.objects.filter(username = user.username).first()
                context = {
                    'fotos':link,
                    'kullanici':rand1.username,
                    'reyting':rand1.reyting,
                    'fotos2':link2,
                    'kullanici2':rand2.username,
                    'reyting2':rand2.reyting,
                    'res':res,
                    'a':a,
                    'b':b,
                }

                return render(request, 'pages/flow.html',context) 


            rand1 = Photo.objects.get(photo_name = resim1)
            rand1.shows +=1
            rand1.reyting +=1
            rand1.performance = int(rand1.reyting/rand1.shows*100)
            rand1.save()

                
            rand2 = random.choice(Photo.objects.filter(Q(performance__lte=rand1.performance+20)&Q(performance__gt=rand1.performance-20)&~Q(photo_name=rand1.photo_name)))
            rand2.shows +=1
            rand2.performance = int(rand2.reyting/rand2.shows*100)
            rand2.save()

            link = 'pages/image/'+rand1.photo_name.name
            link2 = 'pages/image/'+rand2.photo_name.name
            user = request.user

            res = ppUser.objects.filter(username = user.username).first()
            context = {
                'fotos':link,
                'kullanici':rand1.username,
                'reyting':rand1.reyting,
                'fotos2':link2,
                'kullanici2':rand2.username,
                'reyting2':rand2.reyting,
                'res':res,
                'a':a,
                'b':b,
            }

            return render(request, 'pages/flow.html',context)


        elif 'btn2' in request.POST:
            resim2 = request.POST['resim2']
            resim2 = resim2[12:]
            if request.user.is_authenticated and photoLiked.objects.filter(photo_name = resim2 ,username =request.user.username).exists() == False:
                photoLiked.objects.create(username=request.user.username, photo_name=resim2).save()

            b = request.POST['b']
            a = 0
            b = int(b) + 1
            if b == 5:
                b = 0
                rand1 = random.choice(Photo.objects.all())
                rand1.shows +=1
                rand1.performance = int(rand1.reyting/rand1.shows*100)
                rand1.save()

                    
                rand2 = random.choice(Photo.objects.filter(Q(performance__lte=rand1.performance+20)&Q(performance__gt=rand1.performance-20)&~Q(photo_name=rand1.photo_name)))
                rand2.shows +=1
                rand2.performance = int(rand2.reyting/rand2.shows*100)
                rand2.save()

                link = 'pages/image/'+rand1.photo_name.name
                link2 = 'pages/image/'+rand2.photo_name.name
                user = request.user

                res = ppUser.objects.filter(username = user.username).first()
                context = {
                    'fotos':link,
                    'kullanici':rand1.username,
                    'reyting':rand1.reyting,
                    'fotos2':link2,
                    'kullanici2':rand2.username,
                    'reyting2':rand2.reyting,
                    'res':res,
                    'a':a,
                    'b':b,
                }

                return render(request, 'pages/flow.html',context) 

            rand2 = Photo.objects.get(photo_name = resim2)
            rand2.shows +=1
            rand2.reyting +=1
            rand2.performance = int(rand2.reyting/rand2.shows*100)
            rand2.save()

            rand1 = random.choice(Photo.objects.filter(Q(performance__lte=rand2.performance+20)&Q(performance__gt=rand2.performance-20)&~Q(photo_name=rand2.photo_name)))
            rand1.shows +=1
            rand1.performance = int(rand1.reyting/rand1.shows*100)
            rand1.save()


            link = 'pages/image/'+rand1.photo_name.name
            link2 = 'pages/image/'+rand2.photo_name.name
            user = request.user
            res = ppUser.objects.filter(username = user.username).first
            context = {
                'fotos':link,
                'kullanici':rand1.username,
                'reyting':rand1.reyting,
                'fotos2':link2,
                'kullanici2':rand2.username,
                'reyting2':rand2.reyting,
                'res':res,
                'a':a,
                'b':b,
            }

            return render(request, 'pages/flow.html',context) 
        else:
            if 'bildir1' in request.POST:
                resim = request.POST['resim1']
                resim = resim[12:] 
                us = Photo.objects.get(photo_name=resim)      

                feedback.objects.create(complaining = request.user.username,complained= us.username,photo_name = resim).save()
                messages.add_message(request,messages.SUCCESS,"Resim incelenmek üzere listeye alınmıştır. Teşekkürler..")
                return redirect('flow')
            elif 'bildir2' in request.POST:
                resim = request.POST['resim2']
                resim = resim[12:]       
                us = Photo.objects.get(photo_name=resim)      

                feedback.objects.create(complaining = request.user.username,complained= us.username,photo_name = resim).save()
                messages.add_message(request,messages.SUCCESS,"Resim incelenmek üzere listeye alınmıştır. Teşekkürler..")
                return redirect('flow')

            elif 'dnsee1' in request.POST and request.user.is_authenticated:
                resim = request.POST['resim1']
                resim = resim[12:]

                photoBlock.objects.create(username = request.user.username,photo_name = resim).save()
                messages.add_message(request,messages.SUCCESS,"Resim birdaha gösterilmeyecektir.")
                return redirect('flow')
            elif 'dnsee2' in request.POST and request.user.is_authenticated:
                resim = request.POST['resim2']
                resim = resim[12:]

                photoBlock.objects.create(username = request.user.username,photo_name = resim).save()
                messages.add_message(request,messages.SUCCESS,"Resim birdaha gösterilmeyecektir.")
                return redirect('flow')

            elif 'save1' in request.POST and request.user.is_authenticated:
                resim = request.POST['resim1']
                resim = resim[12:]

                photoSave.objects.create(username = request.user.username,photo_name = resim).save()
                messages.add_message(request,messages.SUCCESS,"Resim kaydedilmiştir.")
                return redirect('flow')
            elif 'save2' in request.POST and request.user.is_authenticated:
                resim = request.POST['resim2']
                resim = resim[12:]

                photoSave.objects.create(username = request.user.username,photo_name = resim).save()
                messages.add_message(request,messages.SUCCESS,"Resim kaydedilmiştir.")
                return redirect('flow')

            else:
                return redirect('flow')


    else:
        rand1 = random.choice(Photo.objects.all())

        a = 0
        b = 0
        rand2 = Photo.objects.all().order_by("-yt")[0]
        rand1.shows +=1
        rand1.performance = int(rand1.reyting/rand1.shows*100)
        rand1.save()
        rand2.shows +=1
        rand2.performance = int(rand2.reyting/rand2.shows*100)
        rand2.save()

        link = 'pages/image/'+rand1.photo_name.name
        link2 = 'pages/image/'+rand2.photo_name.name

        user = request.user    
        res = ppUser.objects.filter(username = user.username).first()
        context = {
            'fotos':link,
            'kullanici':rand1.username,
            'reyting':rand1.reyting,
            'fotos2':link2,
            'kullanici2':rand2.username,
            'reyting2':rand2.reyting,
            'res':res,
            'a':a,
            'b':b,
        }

        return render(request, 'pages/flow.html',context) 


def flow2(request):
    if request.method == "POST":
        
        if 'btn1' in request.POST:
            resim1 = request.POST['resim1']
            resim1 = resim1[12:]
            resim2 = request.POST['resim2']
            resim2 = resim2[12:]            
            if request.user.is_authenticated and photoLiked2.objects.filter(photo_name1 = resim1, photo_name2 = resim2 ,username =request.user.username).exists() == False:
                photoLiked2.objects.create(username=request.user.username, photo_name1=resim1, photo_name2 = resim2).save()

            resim = Photo2.objects.get(photo_name1 = resim1,photo_name2 = resim2)
            resim.reyting +=1
            resim.save()

            rand = random.choice(Photo2.objects.filter(hide = 0))
            rand.shows +=1
            rand.save()
            if rand.reyting +rand.reyting2 == 0:
                rey1=50
                rey2=50
            else:
                rey1 = int(rand.reyting *100 / (rand.reyting+rand.reyting2))
                rey2 = int(rand.reyting2 *100 / (rand.reyting+rand.reyting2))
                if rey1+rey2 ==99:
                    rey1+=1

            link = 'pages/image/'+rand.photo_name1.name
            link2 = 'pages/image/'+rand.photo_name2.name
            user = request.user
            res = ppUser.objects.filter(username = user.username).first()
            context = {
                'fotos':link,
                'kullanici':rand.username,
                'reyting':rand.reyting,
                'fotos2':link2,
                'reyting2':rand.reyting2,
                'res':res,
                'rey1':rey1,
                'rey2':rey2,
            }
            return render(request, 'pages/flow2.html',context)


        elif 'btn2' in request.POST:
            resim1 = request.POST['resim1']
            resim1 = resim1[12:]
            resim2 = request.POST['resim2']
            resim2 = resim2[12:]
            if request.user.is_authenticated and photoLiked2.objects.filter(photo_name1 = resim1, photo_name2 = resim2 ,username =request.user.username).exists() == False:
                photoLiked2.objects.create(username=request.user.username, photo_name1=resim1, photo_name2 = resim2).save()

            resim = Photo2.objects.get(photo_name1 = resim1,photo_name2 = resim2)
            resim.reyting2 +=1
            resim.save()


            rand = random.choice(Photo2.objects.filter(hide = 0))
            rand.shows +=1
            rand.save()

            if rand.reyting +rand.reyting2 == 0:
                rey1=50
                rey2=50
            else:
                rey1 = int(rand.reyting *100 / (rand.reyting+rand.reyting2))
                rey2 = int(rand.reyting2 *100 / (rand.reyting+rand.reyting2))
                if rey1+rey2 ==99:
                    rey1+=1

            link = 'pages/image/'+rand.photo_name1.name
            link2 = 'pages/image/'+rand.photo_name2.name
            user = request.user
            res = ppUser.objects.filter(username = user.username).first()
            context = {
                'fotos':link,
                'kullanici':rand.username,
                'reyting':rand.reyting,
                'fotos2':link2,
                'reyting2':rand.reyting2,
                'res':res,
                'rey1':rey1,
                'rey2':rey2,
            }
            return render(request, 'pages/flow2.html',context) 
        elif 'bildir' in request.POST:
            resim1 = request.POST['resim1']
            resim1 = resim1[12:]
            resim2 = request.POST['resim2']
            resim2 = resim2[12:]                    
            resim = Photo2.objects.get(photo_name1 = resim1,photo_name2 = resim2)

            feedback.objects.create(complaining = request.user.username,complained= resim.username,photo_name = resim1,photo_name2 = resim2).save()
            messages.add_message(request,messages.SUCCESS,"Resim incelenmek üzere listeye alınmıştır. Teşekkürler..")
            return redirect('flow2')

        elif 'dnsee' in request.POST and request.user.is_authenticated:
            resim1 = request.POST['resim1']
            resim1 = resim1[12:]
            resim2 = request.POST['resim2']
            resim2 = resim2[12:]

            photoBlock2.objects.create(username = request.user.username,photo_name1 = resim1,photo_name2 = resim2).save()
            messages.add_message(request,messages.SUCCESS,"Resim bir daha gösterilmeyecektir.")
            return redirect('flow2')
                        
    else:
        rand = random.choice(Photo2.objects.filter(hide = 0))
        rand.save()

        if rand.reyting +rand.reyting2 == 0:
            rey1=50
            rey2=50
        else:
            rey1 = int(rand.reyting *100 / (rand.reyting+rand.reyting2))
            rey2 = int(rand.reyting2 *100 / (rand.reyting+rand.reyting2))
            if rey1+rey2 ==99:
                rey1+=1

        link = 'pages/image/'+rand.photo_name1.name
        link2 = 'pages/image/'+rand.photo_name2.name
        user = request.user
        res = ppUser.objects.filter(username = user.username).first()
        context = {
            'fotos':link,
            'kullanici':rand.username,
            'reyting':rand.reyting,
            'fotos2':link2,
            'reyting2':rand.reyting2,
            'res':res,
            'rey1':rey1,
            'rey2':rey2,
        }
        return render(request, 'pages/flow2.html',context) 


def reyting(request):
    user = request.user
    res = ppUser.objects.filter(username = user).first()
    win = Photo.objects.all().order_by("-reyting")[0]
    fotos = Photo.objects.all().order_by("-reyting")[1:20]
    index = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    liste = zip(fotos,index)
    context = {
        'liste':liste,
        'res':res,
        'win':win,
    }
    return render(request, 'pages/reyting.html',context)


def search(request):
    search = request.GET.get('search')
    user = request.user
    res = ppUser.objects.filter(username = user.username).first()
    #unaccent özelliği yüklenemedi
    userss =User.objects.all()
    ppss = ppUser.objects.all()
    #|Q(first_name__icontains= search)|Q(last_name__icontains = search)
    users = userss.filter(username__icontains = search,is_superuser = 0).distinct().order_by('username')
    pps = ppss.filter(username__icontains = search).distinct().order_by('username')
    liste = zip(users,pps)
    
    context = {
        'users':users,
        'pps':pps,
        'liste':liste,
        'res':res
    }
    return render(request,'pages/search.html',context)


def profiles(request,username):
    user = request.user
    fakeuser = User.objects.filter(username = username).first()
    userpp = ppUser.objects.filter(username = username).first()
    photos = Photo.objects.filter(username = username).order_by("-yt")
    photos2 = Photo2.objects.filter(username = username,hide = 0).order_by("-yt")
    fotoslen = len(photos) + len(photos2)
    takipci = followEvent.objects.filter(followed = username)
    takipcilen = len(takipci)
    takip = followEvent.objects.filter(following = username)
    takiplen = len(takip)
       
    a = False
    if user.username != username:
        a = True
    i = False
    if followEvent.objects.filter(following = user.username, followed = username).exists():
        i=True


    if request.method == 'POST':
        if 'btn1' in request.POST:
            resim1 = request.POST['resim1']
            resim2 = request.POST['resim2']
            resim = Photo2.objects.get(photo_name1 = resim1,photo_name2 = resim2)
            resim.reyting +=1
            resim.save()

            rand = random.choice(Photo2.objects.filter(hide = 0))
            rand.shows +=1
            rand.save()
            if rand.reyting +rand.reyting2 == 0:
                rey1=50
                rey2=50
            else:
                rey1 = int(rand.reyting *100 / (rand.reyting+rand.reyting2))
                rey2 = int(rand.reyting2 *100 / (rand.reyting+rand.reyting2))
                if rey1+rey2 ==99:
                    rey1+=1

            link = 'pages/image/'+rand.photo_name1.name
            link2 = 'pages/image/'+rand.photo_name2.name
            user = request.user
            res = ppUser.objects.filter(username = user.username).first()
            context = {
                'fotos':link,
                'kullanici':rand.username,
                'reyting':rand.reyting,
                'fotos2':link2,
                'reyting2':rand.reyting2,
                'res':res,
                'rey1':rey1,
                'rey2':rey2,
            }
            return render(request, 'pages/profiles.html',context)


        elif 'btn2' in request.POST:
            resim1 = request.POST['resim1']
            resim1 = resim1[12:]
            resim2 = request.POST['resim2']
            resim2 = resim2[12:]
            resim = Photo2.objects.get(photo_name1 = resim1,photo_name2 = resim2)
            resim.reyting2 +=1
            resim.save()


            rand = random.choice(Photo2.objects.filter(hide = 0))
            rand.shows +=1
            rand.save()

            if rand.reyting +rand.reyting2 == 0:
                rey1=50
                rey2=50
            else:
                rey1 = int(rand.reyting *100 / (rand.reyting+rand.reyting2))
                rey2 = int(rand.reyting2 *100 / (rand.reyting+rand.reyting2))
                if rey1+rey2 ==99:
                    rey1+=1

            link = 'pages/image/'+rand.photo_name1.name
            link2 = 'pages/image/'+rand.photo_name2.name
            user = request.user
            res = ppUser.objects.filter(username = user.username).first()
            context = {
                'fotos':link,
                'kullanici':rand.username,
                'reyting':rand.reyting,
                'fotos2':link2,
                'reyting2':rand.reyting2,
                'res':res,
                'rey1':rey1,
                'rey2':rey2,
            }
            return render(request, 'pages/profiles.html',context) 

        elif 'followbtn' in request.POST:
            if followEvent.objects.filter(following = user.username, followed = username).exists():
                followEvent.objects.filter(following = user.username, followed = username).delete()
                viewing2.objects.filter(following = user.username,followed=username).delete()
                i = False
                if followEvent.objects.filter(following = user.username, followed = username).exists():
                    i=True
                takipci = followEvent.objects.filter(followed = username)
                takipcilen = len(takipci)
                takip = followEvent.objects.filter(following = username)
                takiplen = len(takip)
                   
                res = ppUser.objects.filter(username = user.username).first()
                context = {
                'fakeuser':fakeuser,
                'userpp':userpp,
                'photos':photos,
                'photos2':photos2,
                'fotoslen':fotoslen,
                'res':res,
                'takipci':takipci,
                'takipcilen':takipcilen,
                'takip':takip,
                'takiplen':takiplen,
                'i':i,
                'a':a,
                }
                return render(request, 'pages/profiles.html',context)
    
            else:
                result =followEvent.objects.create(following = user.username, followed = username)
                result.save()
                c = Photo2.objects.filter(username = username)
                for b in c:
                    viewing2.objects.create(following = result.following,followed = result.followed,photo_name=b.photo_name1,photo_name2=b.photo_name2,view=0).save()
                i = False
                if followEvent.objects.filter(following = user.username, followed = username).exists():
                    i=True
                takipci = followEvent.objects.filter(followed = username)
                takipcilen = len(takipci)
                takip = followEvent.objects.filter(following = username)
                takiplen = len(takip)

                res = ppUser.objects.filter(username = user.username).first()
                context = {
                'fakeuser':fakeuser,
                'userpp':userpp,
                'photos':photos,
                'photos2':photos2,
                'fotoslen':fotoslen,
                'res':res,
                'takipci':takipci,
                'takipcilen':takipcilen,
                'takip':takip,
                'takiplen':takiplen,
                'i':i,
                'a':a,
                }
                return render(request, 'pages/profiles.html',context)
                        

    else:
        res = ppUser.objects.filter(username = user.username).first()
        context = {
            'fakeuser':fakeuser,
            'userpp':userpp,
            'photos':photos,
            'photos2':photos2,
            'fotoslen':fotoslen,
            'res':res,
            'takipci':takipci,
            'takipcilen':takipcilen,
            'takip':takip,
            'takiplen':takiplen,
            'i':i,
            'a':a,
        }
        return render(request, 'pages/profiles.html',context)