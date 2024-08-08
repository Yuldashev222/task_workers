from django.contrib import admin
from django.contrib.auth.models import Group, User
from rangefilter.filters import DateRangeFilterBuilder

from apps.main.models import Worker, Department, Position

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


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name'
    )
    search_fields = (
        'name',
    )
    list_display_links = list_display


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
        'position',
        'department',
        ('date_joined', DateRangeFilterBuilder()),
    )
    search_fields = (
        'first_name',
        'last_name',
        'father_name',
    )
    list_display_links = list_display
