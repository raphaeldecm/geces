import logging
from datetime import datetime

from celery import shared_task
from django.shortcuts import get_object_or_404

from geces.academics.models import Enrollment
from geces.core.constants import MONTHLY_DUE_DAY, MONTHLY_VALUE
from geces.finance.models import Invoice

logger = logging.getLogger(__name__)


@shared_task
def create_enrollment_invoices(enrollment_pk):
    """Create the invoices for the enrollment."""
    try:
        enrollment = get_object_or_404(Enrollment, pk=enrollment_pk)

        months_remaining = 12
        if not enrollment.student_group.reference_year > datetime.now().year:
            months_remaining = 13 - enrollment.created_at.month

        for i in range(months_remaining):
            month = enrollment.created_at.month + i
            if months_remaining == 12:
                month = i + 1

            invoice = Invoice.objects.create(
                enrollment=enrollment,
                due_date=datetime(enrollment.student_group.reference_year, month, MONTHLY_DUE_DAY),
                value=MONTHLY_VALUE,
            )
            invoice.save()
        return True
    except Enrollment.DoesNotExist:
        logger.error("Enrollment does not exist.")
    except Exception as e:
        logger.error(f"Error creating enrollment invoices: {e}")
