from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Collection
from tags.models import TaggedItem

# Create your views here.


def say_hello(request):
    collection = Collection.objects.get(pk=11)
    collection.featured_product = None
    # nebo
    # collection.featured_product_id = 1
    collection.save()

    return render(request, 'hello.html', {'name': 'Mosh'})
