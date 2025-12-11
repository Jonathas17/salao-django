from django.contrib import admin
from .models import Service, Stylist, Client, Appointment, GalleryImage

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration_minutes')

@admin.register(Stylist)
class StylistAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('client', 'service', 'stylist', 'date', 'time', 'confirmed')
    list_filter = ('date', 'confirmed')
    search_fields = ('client__name', 'client__phone')

@admin.register(GalleryImage)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')

admin.site.site_header = "Administração do Salão Feminino"
admin.site.site_title = "Painel do Salão"
admin.site.index_title = "Bem-vindo ao Painel Administrativo"
