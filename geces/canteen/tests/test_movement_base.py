from django.test import TestCase


class TestCanteenBase(TestCase):
    def setUp(self) -> None:
        print("setUp")
        return super().setUp()

    def tearDown(self) -> None:
        print("tearDown")
        return super().tearDown()
