from django.contrib import admin
from .models import *

class RiskAdmin(admin.ModelAdmin):
    list_display = ['id', 'position', 'icon', 'risk_description', 'date_posted']

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'description']

class PackageAdmin(admin.ModelAdmin):
    list_display = ['id', 'package_name', 'rate', 'days']

admin.site.register(Risk, RiskAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Package, PackageAdmin)
