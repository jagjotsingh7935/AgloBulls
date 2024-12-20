from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'timestamp', 'due_date')
    list_filter = ('status', 'timestamp')
    search_fields = ('title', 'description')
