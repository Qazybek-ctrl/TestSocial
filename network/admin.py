from django.contrib import admin
from .models import SocialPerson, Post, ImageFilter, PageImage, Comments
# Register your models here.

admin.site.register(PageImage)
admin.site.register(ImageFilter)
admin.site.register(SocialPerson)
admin.site.register(Post)
admin.site.register(Comments)