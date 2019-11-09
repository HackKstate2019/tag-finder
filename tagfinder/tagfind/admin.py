from django.contrib import admin
from .models import Website,Tag

# Register your models here.

admin.site.site_header="Tag-Finder Admin"
admin.site.site_title="Administrator"
admin.site.index_title="Welcome to the Tag-Finder Admin Area"

class TagInline(admin.TabularInline):
    model=Tag
    extra=1

class WebsiteAdmin(admin.ModelAdmin):
    fieldsets=[('URL',{'fields':['url']}),
    ('Title',{'fields':['title']}),
    ]
    inlines=[TagInline]

admin.site.register(Website,WebsiteAdmin)