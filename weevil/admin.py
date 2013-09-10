from django.contrib import admin
import weevil.models as m

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'magazine', 'author', 'illustrator')
    list_filter = ('magazine', 'author', 'illustrator',)
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}

class ContributorAdmin(admin.ModelAdmin):
    list_dispay = ('name',)
    list_filter = ('articles_written__magazine',)
    search_fields = ('name',)

class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(m.Magazine)
admin.site.register(m.Contributor, ContributorAdmin)
admin.site.register(m.Article, ArticleAdmin)
admin.site.register(m.News, NewsAdmin)
admin.site.register(m.Committee)

