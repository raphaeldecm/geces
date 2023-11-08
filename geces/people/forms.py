
# from django import forms

# from .models import Student


# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = ['name', 'email', 'phone_number', 'address']

#     name = forms.CharField(label='Nome')
#     email = forms.EmailField(label='E-mail')
#     phone_number = forms.CharField(label='Telefone')
#     address = forms.CharField(label='Endereço')

#     def clean_phone_number(self):
#         phone_number = self.cleaned_data['phone_number']
#         if not phone_number.isdigit():
#             raise forms.ValidationError('O número de telefone deve conter apenas números.')
#         return phone_number
