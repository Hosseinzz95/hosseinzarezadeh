from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','published','created_at')
    list_filter = ('published',)
    search_fields = ('title','short_description')
