from django.contrib.auth import authenticate
from ninja import NinjaAPI, Schema
from ninja.security import HttpBasicAuth, HttpBearer
from .models import *
from typing import List, Optional, Union, Literal
import secrets

api = NinjaAPI()


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

