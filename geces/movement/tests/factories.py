import factory
from factory import Faker
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyDecimal, FuzzyInteger

from geces.movement import models
from geces.users.tests.factories import UserFactory


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = models.Product

    created_by = factory.SubFactory(UserFactory)
    name = Faker("name")
    price = FuzzyDecimal(0.01, 1000.00)
    stock = FuzzyInteger(0, 1000)
    image = factory.django.ImageField()
