from django.contrib import admin

from ndfapp.models import Service, Contact, Avis


class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "date_send")

class AvisAdmin(admin.ModelAdmin):
    list_display = ("name", "date", "great")

admin.site.register(Service),
admin.site.register(Contact, ContactAdmin),
admin.site.register(Avis, AvisAdmin),
