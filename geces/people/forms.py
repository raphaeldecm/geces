from django import forms

from .models import Address, Responsible, Student


class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ["city", "address", "zip_code", "phone"]
    
    city = forms.CharField(
        label='Cidade',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )
    address = forms.CharField(
        label='Endereço',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )
    zip_code = forms.CharField(
        label='CEP',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )
    phone = forms.CharField(
        label='Telefone',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )


class ResponsibleForm(forms.ModelForm):
    class Meta:
        model = Responsible
        fields = ["id", "name", "gender", "email"]

    name = forms.CharField(
        label='Nome',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )
    email = forms.EmailField(
        label='E-mail',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )
    phone_number = forms.CharField(
        label='Telefone',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )
    gender = forms.ChoiceField(
        choices=Responsible.Gender.choices,
        label="Gênero",
        widget=forms.Select(
            attrs={
                "class": "form-control",
            }
        )
    )


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'phone_number', 'address']

    name = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail')
    phone_number = forms.CharField(label='Telefone')
    address = forms.CharField(label='Endereço')

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if not phone_number.isdigit():
            raise forms.ValidationError('O número de telefone deve conter apenas números.')
        return phone_number
