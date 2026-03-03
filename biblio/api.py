from django.contrib.auth import authenticate
from ninja import NinjaAPI, Schema
from ninja.security import HttpBasicAuth, HttpBearer
from .models import *
from typing import List, Optional, Union, Literal
import secrets

api = NinjaAPI()

# COMMON: AUTH
###################################

# Autenticació bàsica
class BasicAuth(HttpBasicAuth):
    def authenticate(self, request, username, password):
        user = authenticate(username=username, password=password)
        if user:
            # Genera un token simple
            token = secrets.token_hex(16)
            user.auth_token = token
            user.save()
            return token
        return None

# Autenticació per Token Bearer
class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        try:
            user = Usuari.objects.get(auth_token=token)
            return user
        except Usuari.DoesNotExist:
            return None

# Endpoint per obtenir un token
@api.get("/token", auth=BasicAuth())
@api.get("/token/", auth=BasicAuth())
def obtenir_token(request):
    return {"token": request.auth}


# APP
###################################

class LlibreOut(Schema):
    id: int
    titol: str
    autor: str
    resum: Optional[str]

@api.get("/llibres", response=List[LlibreOut])
@api.get("/llibres/", response=List[LlibreOut])
def obtenir_libres(request):
    qs = Llibre.objects.all()
    return qs

@api.get("/mesllibres", response=List[LlibreOut], auth=AuthBearer())
@api.get("/mesllibres/", response=List[LlibreOut], auth=AuthBearer())
def obtenir_libres(request):
    qs = Llibre.objects.all()
    return qs

