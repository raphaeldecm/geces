from io import BytesIO

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from reportlab.pdfgen import canvas

from geces.academics.models import Enrollment
from geces.finance.models import Invoice


# TODO: Include pix qr code in the invoice
# Create your views here.
def invoice_list_pdf(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)
    invoices = Invoice.objects.filter(enrollment=enrollment)

    buffer = BytesIO()

    pdf = canvas.Canvas(buffer)
    pdf.setTitle(f"Invoices for Enrollment {enrollment.code}")

    # Configurações de estilo
    pdf.setFont("Helvetica", 12)
    page_width, page_height = 595, 842
    margin = 50
    rect_width = (page_width - 3 * margin) / 2
    rect_height = 100
    y_coordinate = page_height - margin

    for index, invoice in enumerate(invoices, start=1):
        if index % 2 != 0:  # Cria um par de retângulos para cada invoice
            x_coordinate = margin
        else:
            x_coordinate = page_width / 2 + margin

        # Desenha os retângulos
        pdf.rect(x_coordinate, y_coordinate - rect_height, rect_width, rect_height)

        # Define as informações dentro dos retângulos
        text_x = x_coordinate + 10
        text_y = y_coordinate - rect_height + 80
        pdf.drawString(text_x, text_y, f"Enrollment Code: {enrollment.code}")
        pdf.drawString(text_x, text_y - 20, f"Student: {enrollment.student.name}")
        pdf.drawString(text_x, text_y - 40, f"Serie: {enrollment.student_group.serie}")
        pdf.drawString(text_x, text_y - 60, f"Due Date: {invoice.due_date}")
        pdf.drawString(text_x, text_y - 80, f"Invoice Number: {index}/{len(invoices)}")
        pdf.drawString(text_x, text_y - 100, f"Value: {invoice.value}")
        pdf.drawString(text_x, text_y - 120, "Payment Date: ____/____/______")

        if index % 2 == 0:  # Se já desenhou o par de retângulos, move para a próxima linha
            y_coordinate -= rect_height + 40  # Espaço entre os pares de retângulos
        # else: permanece na mesma linha para o próximo par de retângulos

    pdf.save()

    # Prepara o PDF para resposta HTTP
    buffer.seek(0)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="invoices_for_{enrollment.code}.pdf"'
    response.write(buffer.getvalue())
    return response
