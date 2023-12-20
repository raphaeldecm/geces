from django.urls import path

from geces.finance import views

app_name = "finance"
urlpatterns = [
    path("invoices/<int:pk>/", views.invoice_list_pdf, name="invoice_list"),
]
