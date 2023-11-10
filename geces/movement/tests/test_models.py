from .factories import ProductFactory
from .test_movement_base import TestMovementBase


class TestMovementModels(TestMovementBase):

    def test_product_str_rep(self):
        print('test_product_str_rep')
        product = ProductFactory()
        self.assertEqual(str(product), product.name)

    def test_product_str_rep_2(self):
        print('test_product_str_rep_2')
        product = ProductFactory()
        self.assertEqual(str(product), product.name)
