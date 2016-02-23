from django.contrib import admin
from app import models

class BBS_admin(admin.ModelAdmin):
    list_display = ('title', 'summary', 'author', 'view_count', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'author__user__username')

admin.site.register(models.BBS, BBS_admin)
admin.site.register(models.Category)
admin.site.register(models.BBS_user)
admin.site.register(models.Comment)

