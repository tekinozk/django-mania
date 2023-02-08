from django.contrib import admin
from blog.models import BlogCategory,BlogTag,Post

@admin.register(BlogTag)
class BlogTagAdmin(admin.ModelAdmin):
    pass


@admin.register(BlogCategory)
class BlogTagAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class BlogTagAdmin(admin.ModelAdmin):
    list_display=[
        "title",
        "is_active",
        "pk",
        "created_at",
        "updated_at",
    ]