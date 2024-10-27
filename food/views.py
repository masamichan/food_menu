from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.
def index(request):
  Item_list = Item.objects.all()
  return HttpResponse(Item_list)

def item(request):
  return HttpResponse('This is an item view')

