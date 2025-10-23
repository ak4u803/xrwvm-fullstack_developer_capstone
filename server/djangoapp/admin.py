from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.

class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1


class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year', 'created_at')
    list_filter = ('car_make', 'type', 'year', 'created_at')
    search_fields = ('name', 'car_make__name')
    ordering = ('car_make', 'name')


class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('name',)
    inlines = [CarModelInline]


# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
