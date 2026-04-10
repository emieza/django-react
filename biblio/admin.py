from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

from .models import *


class UsuariAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
            ("Altres dades (API auth)", {
                'fields': ('auth_token',),
            }),
    )
    readonly_fields = ["auth_token",]


class ImatgeInline(admin.TabularInline):
    readonly_fields = ("imatge_html",)
    fields = ("imatge_html","arxiu","desc",)
    model = Imatge
    extra = 2
    def imatge_html(self,obj):
        return format_html("<img src='{}' width=100 />",obj.arxiu.url)

class LlibreAdmin(admin.ModelAdmin):
    exclude = ()
    inlines = [ImatgeInline,]

admin.site.register(Llibre,LlibreAdmin)
admin.site.register(Usuari,UsuariAdmin)
admin.site.register(Imatge)
