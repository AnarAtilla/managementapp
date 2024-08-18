from django.contrib import admin
from .models import User, Project, Task, Document

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'position', 'project', 'is_active')
    search_fields = ('username', 'email', 'position')
    list_filter = ('position', 'project', 'is_active')
    readonly_fields = ('date_joined', 'last_login', 'updated_at')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status', 'priority', 'created_at', 'project', 'user')
    search_fields = ('title', 'description')
    list_filter = ('status', 'priority', 'project', 'user', 'created_at')
    readonly_fields = ('created_at',)

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'file', 'uploaded_at', 'project')
    search_fields = ('title',)
    list_filter = ('uploaded_at', 'project')
    readonly_fields = ('uploaded_at',)