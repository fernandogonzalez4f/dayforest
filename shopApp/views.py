from django.shortcuts import render
from django.http import HttpResponse
from django.templatetags.static import static
from shopApp.models import Product, Contact

# Create your views here.
def index(request):
    product_list = Product.objects.all()
    special_offers = Product.objects.filter(product_is_offer=True)
    my_context = {
        'user' : 'Fer',
        'message' : '¿Qué tal?',
        'special_offers' : special_offers,
        'product_list' : product_list,
        'special_offers_2' : [
            {
                'name' : 'Audifonos Bluetooth',
                'cost' : 54.00,
                'image' : static('shopApp/img/audifonos_inalambricos_sony.jpg')
            },
            {
                'name' : 'Tablet Samsung Galaxy Tab A9+',
                'cost' : 195.00,
                'image' : static('shopApp/img/tablet_galaxy_tab_9plus.jpg')
            },
            {
                'name' : 'Termo de 1 litro',
                'cost' : 8.00,
                'image' : static('shopApp/img/termo.jpg')
            },
            {
                'name' : 'Lampara',
                'cost' : 24.00,
                'image' : static('shopApp/img/lampara.jpg')
            },
            {
                'name' : 'Mochila para laptop',
                'cost' : 30.00,
                'image' : static('shopApp/img/mochila_laptop.png')
            },
            {
                'name' : 'Soporte para celular',
                'cost' : 9.00,
                'image' : static('shopApp/img/soporte_celular.jpg')
            },
            {
                'name' : 'Otra cosa',
                'cost' : 26.00,
                'image' : static('shopApp/img/otro.jpg')
            },
                    
        ],
        'productos' : [
            '',
            '',
            '',
            '',
            '',
            '',
        ],
    }
    return render(request, 'shopApp/index.html', context=my_context)
    #return HttpResponse("Hola mundo desde Django")

def about(request):
    return render(request, 'shopApp/about.html')  

def about(request):
    #Muestra los contactos activos
    active_contacts = Contact.objects.filter(contact_active=True)
    context = {
        'active_contacts': active_contacts
    }
    return render(request, 'shopApp/about.html', context=context)  