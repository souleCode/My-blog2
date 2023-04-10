from django.contrib import admin
from .models import Post,Comment,Category

# Register your models here.
# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','status','created','publish','author')
    prepopulated_fields = {'slug':('title',)}
    search_fields = ('title','body')
    ordering = ('author','publish')
    list_filter = ('author','publish','created')
    

# admin.site.register(Comment)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_dispaly = ('username', 'email', 'created')
    
admin.site.register(Category)   
prepopulated_fields = {'slug':('name ',)}