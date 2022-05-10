from django.contrib import admin
from .models import Photo, Photo2, ppUser, viewing2,feedback,followEvent,photoBlock,photoBlock2,photoLiked,photoLiked2,photoSave


# Register your models here.
    

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id','userid','username','photo_name','reyting','shows','performance','yt')
    list_filter = ('yt',)
    search_fields = ('userid',)
    ordering = ('-reyting',)

class PhotoAdmin2(admin.ModelAdmin):
    list_display = ('id','username','photo_name1','photo_name2','reyting','shows','yt','hide')
    list_filter = ('yt',)
    search_fields = ('userid',)
    ordering = ('-reyting',)

class viewing2Admin(admin.ModelAdmin):
    list_display = ('id','following','followed','photo_name','photo_name2','view')
    search_fields = ('view',)

class ppUserAdmin(admin.ModelAdmin):
    list_display = ('id','username','pp')
    list_filter = ('username',)
    search_fields = ('username',)

class followEventAdmin(admin.ModelAdmin):
    list_display = ('id','following','followed')

class feedbackAdmin(admin.ModelAdmin):
    list_display = ('id','complaining','complained','photo_name','photo_name2')
    search_fields = ('photo_name','photo_name2',)

class photoBlockAdmin(admin.ModelAdmin):
    list_display = ('id','username','photo_name')
    search_fields = ('username','photo_name')
    
class photoLikedAdmin(admin.ModelAdmin):
    list_display = ('id','username','photo_name')
    search_fields = ('username','photo_name')

class photoSaveAdmin(admin.ModelAdmin):
    list_display = ('id','username','photo_name')
    search_fields = ('username',)
    
class photoBlock2Admin(admin.ModelAdmin):
    list_display = ('id','username','photo_name1','photo_name2')
    search_fields = ('username','photo_name','photo_name2')

class photoLiked2Admin(admin.ModelAdmin):
    list_display = ('id','username','photo_name1','photo_name2')
    search_fields = ('username','photo_name','photo_name2')




admin.site.register(Photo,PhotoAdmin)
admin.site.register(Photo2,PhotoAdmin2)
admin.site.register(viewing2,viewing2Admin)
admin.site.register(ppUser,ppUserAdmin)
admin.site.register(followEvent,followEventAdmin)
admin.site.register(feedback,feedbackAdmin)
admin.site.register(photoBlock,photoBlockAdmin)
admin.site.register(photoBlock2,photoBlock2Admin)
admin.site.register(photoLiked,photoLikedAdmin)
admin.site.register(photoLiked2,photoLiked2Admin)
admin.site.register(photoSave,photoSaveAdmin)