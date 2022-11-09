from django.contrib import admin
from .models import Categories , Videos , LikedVideos , Subscriptions , WatchLater 

# this is the complete error
# Register your models here.

admin.site.register(Categories)
admin.site.register(Videos)
admin.site.register(LikedVideos)
admin.site.register(Subscriptions)
admin.site.register(WatchLater)


