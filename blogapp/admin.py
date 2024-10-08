from django.contrib import admin
from .models import Post, Comment


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 
                    'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    
admin.site.register(Post,PostAdmin) 

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','email','post','created','active')
    search_fields = ('name','emial','body')
    list_filter = ('active','created','updated')

admin.site.register(Comment,CommentAdmin)
