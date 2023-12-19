from datetime import datetime

from django.db.models.signals import post_save
from django.dispatch import receiver

from geces.academics.models import Enrollment
from geces.core.constants import MONTHLY_DUE_DAY, MONTHLY_VALUE
from geces.finance.models import Invoice


@receiver(post_save, sender=Enrollment)
def enrollment_created(sender, instance, created, **kwargs):
    if created:
        months_remaining = 12
        if not instance.student_group.reference_year > datetime.now().year:
            months_remaining = 12 - instance.created_at.month + 1

        for i in range(months_remaining):
            print("## ", i)
            invoice = Invoice.objects.create(
                enrollment=instance,
                due_date=datetime(
                    instance.student_group.reference_year,
                    i+1,
                    MONTHLY_DUE_DAY),
                value=MONTHLY_VALUE,
            )
            print("## ", invoice)
            invoice.save()
