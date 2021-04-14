from django.contrib import admin
from blogs.models import Post, BlogComment
# Register your models here.
admin.site.register((BlogComment))
#Register Model here
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js=('javascript/tiny.js',)