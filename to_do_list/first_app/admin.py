from django.contrib import admin
from . models import AddTask
# Register your models here.

@admin.register(AddTask)
class Task(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date')