from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(WorkPlace)
admin.site.register(WorkPlaceImage)
admin.site.register(VideoUrl)
admin.site.register(ResponseForMaster)
admin.site.register(Sketch)
admin.site.register(LikeScketch)
admin.site.register(CommentSketch)
admin.site.register(LikeCommentSketch)
# Register your models here.
