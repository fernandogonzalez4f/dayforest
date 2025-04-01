from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.templatetags.static import static
from shopApp.models import Product, Contact
from shopApp.forms import FormComment, ContactForm

# Create your views here.
def index(request):
    product_list = Product.objects.all()
    special_offers = Product.objects.filter(product_is_offer=True)
    my_context = {
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
    contact_list = Contact.objects.filter(contact_active=True).order_by("contact_full_name")
    return render(request, 'shopApp/about.html', context={'contacts' : contact_list})

def form_comment(request):
    form = FormComment()

    if request.method == 'POST':
        form = FormComment(request.POST)
        if form.is_valid():
            print('Formulario valido')
            print('Nombre: ', form.cleaned_data['full_name'])
            print('Email: ', form.cleaned_data['email'])
            print('Comentario: ', form.cleaned_data['comment'])
    return render(request, 'shopApp/form_comment.html', context={'form' : form})

def add_contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact.objects.create(
                contact_full_name=form.cleaned_data['contact_full_name'],
                contact_address=form.cleaned_data['contact_address'],
                contact_phone=form.cleaned_data['contact_phone'],
                contact_email=form.cleaned_data['contact_email'],
                contact_active=form.cleaned_data['contact_active']
            )
            return redirect('about')

    return render(request, 'shopApp/add_contact.html', context={'form': form})