from django import forms

from .models import Person, Responsible, Student


class PersonForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = Person
        fields = ["id", "name", "gender", "email"]


class ResponsibleForm(forms.ModelForm):
    class Meta:
        model = Responsible
        fields = ["person__name", "person__email", "person__phone", "person__gender", "address"]

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone']
        if not phone_number.isdigit():
            raise forms.ValidationError('O número de telefone deve conter apenas números.')
        return phone_number


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
