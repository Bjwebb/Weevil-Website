from django.contrib import admin
import weevil.models as m
from adminsortable.admin import SortableTabularInline, SortableAdmin

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'magazine', 'author', 'illustrator')
    list_filter = ('magazine', 'author', 'illustrator',)
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}

class ArticleInline(SortableTabularInline):
    model = m.Article

class MagazineAdmin(SortableAdmin):
    inlines = [
        ArticleInline,
    ]

class ContributorAdmin(admin.ModelAdmin):
    list_dispay = ('name',)
    list_filter = ('articles_written__magazine',)
    search_fields = ('name',)

class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(m.Magazine, MagazineAdmin)
admin.site.register(m.Contributor, ContributorAdmin)
admin.site.register(m.Article, ArticleAdmin)
admin.site.register(m.News, NewsAdmin)
admin.site.register(m.Committee)

