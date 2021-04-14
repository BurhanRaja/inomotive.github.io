from django.contrib import admin
from projects.models import Project
# Register your models here.
#admin.site.register((projectComment))
#Register Model here
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    class Media:
        js=('images/tiny.js',)