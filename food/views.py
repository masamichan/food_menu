from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader

# Create your views here.
def index(request):
  Item_list = Item.objects.all()
  context = {
      'item_list':Item_list
  }
  return render(request, 'food/index.html', context)

def item(request):
  return HttpResponse('This is an item view')

