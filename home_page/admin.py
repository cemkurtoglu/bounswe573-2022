from django.contrib import admin
from home_page.models import *

admin.site.register(Comments)
admin.site.register(Post)
admin.site.register(PostDislikes)
admin.site.register(PostLikes)
admin.site.register(Tags)