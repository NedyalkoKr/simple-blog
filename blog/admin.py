from django.contrib import admin
from blog.models import Post

# Register your models here.

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish', 'created', 'updated', 'status',)
    list_filter = ('status', 'created', 'publish', 'author',)
    prepopulated_fields = {
        'slug': ('title',)
    }
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')