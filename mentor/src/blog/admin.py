from django.contrib import admin
from blog.models import Blog, BlogImage


class BlogImageInline(admin.TabularInline):
    extra = 0
    model = BlogImage


class BlogAdmin(admin.ModelAdmin):
    inlines = [
        BlogImageInline,
    ]


admin.site.register(Blog, BlogAdmin)
