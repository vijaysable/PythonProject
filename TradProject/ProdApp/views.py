from django.shortcuts import render
from .models import Products
# Create your views here.
# from ..UserApp.models import Users


def post(request):
    if request.method == 'POST':
        r = request.POST
        p = Products()
        p.name = r.get('name')
        p.price = r.get('quantity1')
        p.weight = r.get('quantity2')
        p.save()
    context = {'post': Products.objects.all()}
    return render(request, 'ProdApp/Posting.html', context)
