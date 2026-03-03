from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *


class UsuariAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
            ("Altres dades (API auth)", {
                'fields': ('auth_token',),
            }),
    )
    readonly_fields = ["auth_token",]


admin.site.register(Llibre)
admin.site.register(Usuari,UsuariAdmin)
