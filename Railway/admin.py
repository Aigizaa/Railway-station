from django.contrib import admin
from Railway.models import Schedule, Train
# Register your models here.
@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    pass


@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    pass
