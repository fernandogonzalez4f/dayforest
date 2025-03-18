#Cargar los elementos necesarios para utilizar los modulos de django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dayforest.settings')
import django
django.setup()

#Script para poblar la tabla Contact
from faker import Faker
import random
from shopApp.models import Contact

fake_generator = Faker()

def populate_contacts(n_contacts = 10):
    for i in range(n_contacts): 
        fake_full_name = fake_generator.name()
        fake_address = fake_generator.address()
        fake_phone = fake_generator.phone_number()
        fake_email = fake_generator.email()
        fake_active = random.choice([True, False])
        
        contact = Contact.objects.get_or_create(
            contact_full_name = fake_full_name,
            contact_address = fake_address,
            contact_phone = fake_phone,
            contact_email = fake_email,
            contact_active = fake_active
        )

if __name__ == '__main__':
    print('Empezar a poblar la base de datos con contactos.')
    populate_contacts(30)
    print('Finalizado.')