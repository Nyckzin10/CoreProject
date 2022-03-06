from django.contrib import admin
from .models import Category, Post, Comment





class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}




class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category','image_table',]
    readonly_fields = ('image_table',)
    list_filter = ['slug'] 
    prepopulated_fields = {'slug': ('title',)}





class CommentAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['status']





##admin.site.unregister(Post)
admin.site.register(Post,PostAdmin)
##admin.site.unregister(Category)
admin.site.register(Category,CategoryAdmin)
##admin.site.unregister(Comment)
admin.site.register(Comment, CommentAdmin)