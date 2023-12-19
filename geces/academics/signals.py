import logging

from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from geces.academics.models import Enrollment
from geces.academics.tasks import create_enrollment_invoices

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Enrollment)
def enrollment_created(sender, instance, created, **kwargs):
    if created:
        try:
            print("creating enrollment invoices")
            transaction.on_commit(
                lambda: create_enrollment_invoices.delay(instance.pk)
            )
        except Exception as e:
            logger.error(f"Error creating enrollment invoices: {e}")
