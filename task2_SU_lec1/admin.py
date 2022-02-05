from django.contrib import admin
from task2_SU_lec1.models import Task


# admin.site.register(Task)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_title', 'task_text')
