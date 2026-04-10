from django.contrib.auth import authenticate
from ninja import NinjaAPI, Schema
from ninja.security import HttpBasicAuth, HttpBearer
from django.shortcuts import get_object_or_404
from typing import List, Optional, Union, Literal
import secrets, datetime

from .models import *

api = NinjaAPI()


class ImatgeOut(Schema):
    id: int
    arxiu: str

class LlibreOut(Schema):
    id: int
    titol: str
    autor: str
    data_edicio: datetime.date
    resum: Optional[str]

class LlibreComplertOut(Schema):
    id: int
    titol: str
    autor: str
    data_edicio: datetime.date
    resum: Optional[str]
    imatge_set: List[ImatgeOut]

@api.get("/llibres", response=List[LlibreOut])
@api.get("/llibres/", response=List[LlibreOut])
def obtenir_libres(request):
    qs = Llibre.objects.all()
    return qs

@api.get("/llibre/{id}", response=LlibreComplertOut)
@api.get("/llibre/{id}/", response=LlibreComplertOut)
def obtenir_libres(request,id:int):
    llibre = get_object_or_404(Llibre,id=id)
    return llibre
