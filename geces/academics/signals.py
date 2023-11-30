from django.db import IntegrityError
from django.db.models.signals import pre_save
from django.dispatch import receiver

from geces.academics.models import Enrollment, StudentGroup


@receiver(pre_save, sender=Enrollment)
def enrollment_created(sender, instance, **kwargs):
    if not instance.student_group_id:
        try:
            student_group = StudentGroup.objects.create(
                reference_year=instance.enrollment_date.year, serie=instance.serie
            )
            instance.student_group = student_group
            student_group.students.add(instance.student)
        except IntegrityError:
            instance.student_group = StudentGroup.objects.get(
                reference_year=instance.enrollment_date.year, serie=instance.serie
            )
