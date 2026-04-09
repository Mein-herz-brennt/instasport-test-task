from django.contrib import admin
from .models import TrainingSession

@admin.register(TrainingSession)
class TrainingSessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time')
    list_filter = ('start_time',)
    search_fields = ('title',)
