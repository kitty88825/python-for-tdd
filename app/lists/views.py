from django.http import HttpResponse
from django.shortcuts import redirect, render

from app.lists.models import Item, List


def home_page(request) -> HttpResponse:
    return render(request, 'home.html')


def view_list(request, list_id: int) -> HttpResponse:
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})


def new_list(request) -> HttpResponse:
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}')


def add_item(request, list_id: int) -> HttpResponse:
    list_ = List.objects.get(pk=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}')
