from django.http import request
from django.shortcuts import render,redirect
from pages.models import Photo, ppUser, followEvent, Photo2, viewing2,feedback,photoSave
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.db.models import Q
from .forms import uploadForm, uploadppForm, uploadForm2
from django.http import JsonResponse
# Create your views here.   


def register(request):

    if request.method == 'POST':
        fakepp = '44884218_345707102882519_2446069589734326272_n.jpg'
        #öğeleri al
        name = request.POST['name']
        surname = request.POST['surname']
        username = request.POST['username']
        password = request.POST['password']
        repassword = request.POST['repassword']
        email = request.POST['email']
        
        #kontrol

        if password == repassword:
            
            if User.objects.filter(username = username).exists():
                messages.add_message(request,messages.WARNING,'Bu kullanıcı adı kullanılmakta. Başka bir kullanıcı adı girmeyi deneyin')
                return redirect('register')
            else:
                if User.objects.filter(email = email).exists():
                    messages.add_message(request,messages.WARNING,'Bu email kullanılmakta. Başka bir email girmeyi deneyin')
                    return redirect('register')

                else:
                    #kayıt
                    user = User.objects.create_user(first_name = name,last_name = surname, username = username, password = password, email = email)
                    user.save()
                    pp = ppUser.objects.create(username = username, pp = fakepp)
                    pp.save()
                    messages.add_message(request,messages.SUCCESS,'Kullanıcı başarı ile oluşturuldu')
                    return redirect('flow')
        else:
            messages.add_message(request, messages.WARNING, 'Parolalar uyuşmuyor')
            return redirect('register')
    
    
    
    else:
        return render(request, 'user/register.html')


def login(request):  
    #öğeleri al
    username = request.POST['username']
    password = request.POST['password']
    
    #kontrol
    user = auth.authenticate(username = username, password = password)
    if user is not None:
        auth.login(request, user)

        messages.add_message(request, messages.SUCCESS, 'Oturum açıldı')
        return redirect('flow')

    else:
        messages.add_message(request, messages.ERROR, 'Kullanıcı adı veya parola hatalı')
        return redirect('flow')


def logout(request):

    auth.logout(request)
    messages.add_message(request, messages.SUCCESS, 'Oturum kapatıldı')

    return redirect('flow')


def profile(request):
    user = request.user
    fotos = Photo.objects.filter(username = user.username).order_by("-yt")
    fotos2 = Photo2.objects.filter(username = user.username).order_by("-yt")
    fotoslen = len(fotos)+len(fotos2)
    takipci = followEvent.objects.filter(followed = user.username)
    takipcilen = len(takipci)
    takipcipps = []
    for result in takipci:
        pp=ppUser.objects.get(username=result.following).pp
        takipcipps.append(pp)
    takipcilist = zip(takipci,takipcipps)

    takip = followEvent.objects.filter(following = user.username)
    takiplen = len(takip)
    takippps = []
    for result in takip:
        pp=ppUser.objects.get(username=result.followed).pp
        takippps.append(pp)
    takiplist = zip(takip,takippps)

    if 'delete' in request.POST:
        resim =  request.POST['resim']
        Photo.objects.get(username = request.user.username,photo_name=resim).delete()
        messages.add_message(request,messages.SUCCESS,'Resim başarı ile Silindi')
        return redirect('profile')

    elif 'delete2' in request.POST:
        resim1 =  request.POST['resim1']
        resim2 =  request.POST['resim2']
        Photo2.objects.get(username = request.user.username,photo_name1=resim1,photo_name2=resim2).delete()
        viewing2.objects.filter(followed = request.user.username,photo_name=resim1,photo_name2=resim2).delete()
        messages.add_message(request,messages.SUCCESS,'Resim başarı ile Silindi')
        return redirect('profile')

    


    res = ppUser.objects.filter(username = user.username).first()
    context = {
    'fotos':fotos,
    'fotos2':fotos2,
    'fotoslen':fotoslen,
    'res':res,
    'takipci':takipcilist,
    'takipcilen':takipcilen,
    'takip':takiplist,
    'takiplen':takiplen
    }

    return render(request, 'user/profile.html',context)


def saveimage(request):
    user = request.user
    fotos = Photo.objects.filter(username = user.username).order_by("-yt")
    fotos2 = Photo2.objects.filter(username = user.username).order_by("-yt")
    saveFotos = photoSave.objects.filter(username = user.username)
    fotoslen = len(fotos)+len(fotos2)
    takipci = followEvent.objects.filter(followed = user.username)
    takipcilen = len(takipci)
    takipcipps = []
    for result in takipci:
        pp=ppUser.objects.get(username=result.following).pp
        takipcipps.append(pp)
    takipcilist = zip(takipci,takipcipps)

    takip = followEvent.objects.filter(following = user.username)
    takiplen = len(takip)
    takippps = []
    for result in takip:
        pp=ppUser.objects.get(username=result.followed).pp
        takippps.append(pp)
    takiplist = zip(takip,takippps)

    if 'delete' in request.POST:
        resim =  request.POST['resim']
        photoSave.objects.filter(username = request.user.username,photo_name=resim).delete()
        messages.add_message(request,messages.SUCCESS,'Resim başarı ile Silindi')
        return redirect('save')


    res = ppUser.objects.filter(username = user.username).first()
    context = {
    'fotos':saveFotos,
    'fotoslen':fotoslen,
    'res':res,
    'takipci':takipcilist,
    'takipcilen':takipcilen,
    'takip':takiplist,
    'takiplen':takiplen
    }

    return render(request, 'user/saveimage.html',context)



def uploadimage(request):
    user = request.user
    fotos = Photo.objects.filter(username = user.username)
    fotos2 = Photo2.objects.filter(username = user.username)
    fotoslen = len(fotos)+len(fotos2)
    takipci = followEvent.objects.filter(followed = user.username)
    takipcilen = len(takipci)
    takipcipps = []
    for result in takipci:
        pp=ppUser.objects.get(username=result.following).pp
        takipcipps.append(pp)
    takipcilist = zip(takipci,takipcipps)

    takip = followEvent.objects.filter(following = user.username)
    takiplen = len(takip)
    takippps = []
    for result in takip:
        pp=ppUser.objects.get(username=result.followed).pp
        takippps.append(pp)
    takiplist = zip(takip,takippps)


    form = uploadForm(request.POST or None, request.FILES or None)
    form2 = uploadForm2(request.POST or None, request.FILES or None)
    if request.is_ajax():
        if form.is_valid():
            user = request.user
            res = Photo.objects.create(userid = user.pk, username = user.username , photo_name = form['photo_name'].value(), reyting = 0, shows = 0, performance =1)
            res.save()
            messages.add_message(request,messages.SUCCESS,'Resim başarı ile yüklendi')
            return redirect('profile')

        elif form2.is_valid():
            if form2['hide'].value() == '0':
                user = request.user
                res = Photo2.objects.create(username = user.username , photo_name1 = form2['photo_name1'].value(), photo_name2 = form2['photo_name2'].value(), reyting = 0,reyting2 = 0, shows = 0, hide = 0)
                res.save()
                result = followEvent.objects.filter(followed = user.username)
                result.update(photo_true2 = 1)
                for result in result:
                    a = viewing2.objects.create(following = result.following,followed = result.followed,photo_name=res.photo_name1.name,photo_name2=res.photo_name2.name,view=0)
                    a.save()
                messages.add_message(request,messages.SUCCESS,'Resim başarı ile yüklendi')
                return redirect('profile')
                
            elif form2['hide'].value() == '1':
                user = request.user
                res = Photo2.objects.create(username = user.username , photo_name1 = form2['photo_name1'].value(), photo_name2 = form2['photo_name2'].value(), reyting = 0,reyting2 = 0, shows = 0,hide = 1)
                res.save()
                result = followEvent.objects.filter(followed = user.username)
                result.update(photo_true2 = 1)
                for result in result:
                    a = viewing2.objects.create(following = result.following,followed = result.followed,photo_name=res.photo_name1.name,photo_name2=res.photo_name2.name,view=0)
                    a.save()
                messages.add_message(request,messages.SUCCESS,'Resim başarı ile yüklendi')
                return redirect('profile')



    res = ppUser.objects.filter(username = user.username).first()
    context = {
    'fotoslen':fotoslen,
    'res':res,
    'form':form,
    'form2':form2,
    'takipci':takipcilist,
    'takipcilen':takipcilen,
    'takip':takiplist,
    'takiplen':takiplen
    }

    return render(request, 'user/uploadimage.html',context)



def settings(request):
    form = uploadppForm(request.POST or None, request.FILES or None)
    if request.is_ajax():
        print('ajax girdi')
        if form.is_valid():
            print('form girdi')
            resim = form['pp'].value()
            user = request.user

            ppUser.objects.filter(username = user.username).delete()
            resim = ppUser.objects.create(username = user.username, pp = resim)
            resim.save()

            messages.add_message(request,messages.SUCCESS,'Resim başarı ile güncellendi')
            res = ppUser.objects.filter(username = user.username).first()
            return redirect('settings')

    if request.method == 'POST':
        #öğe al
        if 'send' in request.POST:
            name = request.POST['name']
            surname = request.POST['surname']
            sendingusername = request.POST['username']
            email = request.POST['email']

            user = request.user

            if user.username != sendingusername:
                if User.objects.filter(username = sendingusername).exists():
                    messages.add_message(request,messages.WARNING,'Bu kullanıcı adı kullanılmakta. Başka bir kullanıcı adı girmeyi deneyin')
                    return redirect('settings')

                else:
                    if user.email != email:
                    
                        if User.objects.filter(email = email).exists():
                            messages.add_message(request,messages.WARNING,'Bu email kullanılmakta. Başka bir email girmeyi deneyin')
                            return redirect('settings')

                        else:
                            User.objects.filter(username = user.username).update(first_name = name,last_name = surname, username = sendingusername, email = email)
                            Photo.objects.filter(username = user.username).update(username= sendingusername)
                            Photo2.objects.filter(username = user.username).update(username= sendingusername)
                            ppUser.objects.filter(username=user.username).update(username= sendingusername)
                            followEvent.objects.filter(following=user.username).update(following= sendingusername)
                            followEvent.objects.filter(followed=user.username).update(followed= sendingusername)
                            viewing2.objects.filter(following=user.username).update(following= sendingusername)
                            viewing2.objects.filter(followed=user.username).update(followed= sendingusername)
                            feedback.objects.filter(complaining=user.username).update(complaining= sendingusername)
                            feedback.objects.filter(complained=user.username).update(complained= sendingusername)

                            messages.add_message(request,messages.SUCCESS,'kullanıcı başarıyla güncllendi')
                            return redirect('settings')
                    else:
                        User.objects.filter(username = user.username).update(first_name = name,last_name = surname, username = sendingusername)
                        Photo.objects.filter(username = user.username).update(username= sendingusername)
                        Photo2.objects.filter(username = user.username).update(username= sendingusername)
                        ppUser.objects.filter(username=user.username).update(username= sendingusername)
                        followEvent.objects.filter(following=user.username).update(following= sendingusername)
                        followEvent.objects.filter(followed=user.username).update(followed= sendingusername)
                        viewing2.objects.filter(following=user.username).update(following= sendingusername)
                        viewing2.objects.filter(followed=user.username).update(followed= sendingusername)
                        feedback.objects.filter(complaining=user.username).update(complaining= sendingusername)
                        feedback.objects.filter(complained=user.username).update(complained= sendingusername)

                        messages.add_message(request,messages.SUCCESS,'kullanıcı başarıyla güncllendi')
                        return redirect('settings')


            else:
                if user.email != email:
                
                    if User.objects.filter(email = email).exists():
                        messages.add_message(request,messages.WARNING,'Bu email kullanılmakta. Başka bir email girmeyi deneyin')
                        return redirect('settings')

                    else:
                        User.objects.filter(username = user.username).update(first_name = name,last_name = surname, email = email)
                        messages.add_message(request,messages.SUCCESS,'kullanıcı başarıyla güncllendi')
                        return redirect('settings')

                else:
                    User.objects.filter(username = user.username).update(first_name = name, last_name = surname)
                    messages.add_message(request,messages.SUCCESS,'kullanıcı başarıyla güncllendi')
                    return redirect('settings')

        # elif 'ppsend' in request.POST:
        #     resim = request.FILES['pp']

        #     user = request.user

        #     ppUser.objects.filter(username = user.username).delete()
        #     resim = ppUser.objects.create(username = user.username, pp = resim)
        #     resim.save()

        #     messages.add_message(request,messages.SUCCESS,'Resim başarı ile güncellendi')
        #     res = ppUser.objects.filter(username = user.username).first()
        #     context = {
        #         'res':res,
        #         'form':form,
        #     }
        #     return render(request, 'user/settings.html',context)

        elif 'pswsend' in request.POST:
            oldpassword = request.POST['oldpassword']
            password = request.POST['password']
            repassword = request.POST['repassword']

            user = request.user 


            if user.check_password(oldpassword):
                if password == repassword:
                    user.set_password(password)
                    messages.add_message(request,messages.SUCCESS,'Şifreniz güncellenmiştir')
                    return redirect('settings')

                else:
                    messages.add_message(request,messages.WARNING,'Şifreniz uyuşmuyor')
                    return redirect('settings')
            else:
                messages.add_message(request,messages.WARNING,'Şifrenizi yalnış girdiniz')
                return redirect('settings')
                

    else:
        user = request.user

        res = ppUser.objects.filter(username = user.username).first()
        context = {
            'res':res,
            'form':form,
        }
        return render(request, 'user/settings.html',context)

