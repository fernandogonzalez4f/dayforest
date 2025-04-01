from django import forms

class FormComment(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    comment = forms.CharField(widget=forms.Textarea)

class ContactForm(forms.Form):
    contact_full_name = forms.CharField(label="Nombre Completo", max_length=100)
    contact_address = forms.CharField(label="Dirección", max_length=100)
    contact_phone = forms.CharField(label="Teléfono", max_length=20)
    contact_email = forms.EmailField(label="Email")
    contact_active = forms.BooleanField(label="Activo", required=False)