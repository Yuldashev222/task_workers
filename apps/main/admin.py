from django.contrib import admin
from rangefilter.filters import DateRangeFilterBuilder
from django.contrib.auth.models import Group, User

from apps.main.models import Worker, Department

admin.site.unregister([Group, User])


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'parent'
    )
    search_fields = (
        'name',
    )
    list_display_links = list_display
    ordering = ('id',)


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'father_name',
        'position',
        'department',
        'salary',
        'date_joined',
    )
    list_filter = (
        ('date_joined', DateRangeFilterBuilder()),
        'position',
    )
    search_fields = (
        'first_name',
        'last_name',
        'father_name',
    )
    list_display_links = list_display
