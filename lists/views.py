from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List


# Create your views here.
def home_page(request):

    items = Item.objects.all()
    # print("items[0]: ", items[0].text)
    """
        The 1st loading of the webpage is not POST
    """
    return render(request, 'home.html', {'items': items})


    # return HttpResponse('Non-Post: fuck world')

def view_list(request):
    """Fetch items from database"""
    items = Item.objects.all()
    """Put them into webpage: list.html"""
    return render(request, 'list.html', {'items': items})


def new_list(request):
    if request.POST['item_text'] == "":  # Clean Button Click
        items = Item.objects.all()
        for item in items:
            item.delete()
    else:
        # list_ = List.objects.create()
        Item.objects.create(text=request.POST['item_text'])
        # Item.objects.create(text=request.POST['item_text'], list=list_)
    # Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/the_only-list-in-the-world/')

