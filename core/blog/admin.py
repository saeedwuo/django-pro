from django.contrib import admin
from .models import Category,Post
# Register your models here.


class   PostAdmin(admin.ModelAdmin):
    
    list_display = ['author','status','title','created_date','published_date']
    
    
    
    
admin.site.register(Category)
admin.site.register(Post)