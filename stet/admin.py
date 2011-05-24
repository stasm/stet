from django.contrib import admin

from stet.models import Article

class ArticleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Article, ArticleAdmin)
