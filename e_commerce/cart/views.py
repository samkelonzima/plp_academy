from django.shortcuts import render,get_object_or_404
from .models import cart

def cart_details(request):
    cart = get_object_or_404(cart,
pk=request.session.get('cart_id'))
    return render(request, 'cart/cart_detail.html', {'cart': cart})                   


# Create your views here.
