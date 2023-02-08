from django.contrib import admin
from page.models import Page

class PageAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "is_active",
        "created_at",
        "updated_at",
        "pk",
    ]
admin.site.register(Page,PageAdmin)

# Register your models here.
