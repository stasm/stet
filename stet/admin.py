from django.contrib import admin

from stet.models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display_links = ('title',)
    list_display = ('id', 'title', '_status', 'pub_date')
    fieldsets = (
        (None, {
            'fields': ('title', '_status', 'body')
        }),
        ('Meta', {
            'classes': ('collapse',),
            'fields': ('tags', 'excerpt'),
        }),
        ('Under the hood', {
            'classes': ('collapse',),
            'fields': ('pub_date', 'filename', 'html'),
        }),
    )

admin.site.register(Article, ArticleAdmin)
