from django.test import TestCase

# Create your tests here.
from decimal import Decimal
import json


from .models import (
    Box,
    Order,
    OrderItem,
    Product,
)

from .services import (
    dimensions_fit,
    recommend_box,
)


class BoxRecommendationTests(TestCase):

    def setUp(self):

        self.small = Box.objects.create(
            name="Small",
            internal_length_cm=20,
            internal_width_cm=20,
            internal_height_cm=20,
            max_weight_kg=2,
            cost=Decimal("3.00"),
        )

        self.medium = Box.objects.create(
            name="Medium",
            internal_length_cm=40,
            internal_width_cm=30,
            internal_height_cm=25,
            max_weight_kg=10,
            cost=Decimal("5.00"),
        )

        self.large = Box.objects.create(
            name="Large",
            internal_length_cm=60,
            internal_width_cm=50,
            internal_height_cm=40,
            max_weight_kg=20,
            cost=Decimal("8.00"),
        )

    def create_product(
        self,
        **overrides
    ):

        data = {
            "name": "Widget",
            "length_cm": 10,
            "width_cm": 10,
            "height_cm": 10,
            "weight_kg": 1,
        }

        data.update(overrides)

        return Product.objects.create(
            **data
        )

    def test_dimensions_fit_with_rotation(self):

        result = dimensions_fit(
            (30, 20, 10),
            (10, 30, 20),
        )

        self.assertTrue(result)

    def test_selects_cheapest_box(self):

        product = self.create_product()

        order = Order.objects.create()

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=1,
        )

        result = recommend_box(order)

        self.assertEqual(
            result.box,
            self.small
        )

    def test_weight_limit(self):

        product = self.create_product(
            weight_kg=3
        )

        order = Order.objects.create()

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=1,
        )

        result = recommend_box(order)

        self.assertEqual(
            result.box,
            self.medium
        )

    def test_no_box_available(self):

        product = self.create_product(
            length_cm=100,
            width_cm=100,
            height_cm=100,
        )

        order = Order.objects.create()

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=1,
        )

        with self.assertRaisesMessage(
            ValueError,
            "No suitable box found"
        ):
            recommend_box(order)

    def test_empty_order(self):

        order = Order.objects.create()

        with self.assertRaisesMessage(
            ValueError,
            "Order has no items"
        ):
            recommend_box(order)

    def test_api_success(self):

        product = self.create_product()

        order = Order.objects.create()

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=1,
        )

        response = self.client.post(
            "/api/recommend-box/",
            data=json.dumps({
                "order_id": order.id
            }),
            content_type="application/json",
        )

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertEqual(
            response.json()[
                "recommended_box"
            ]["name"],
            "Small",
        )

    def test_invalid_order_id(self):

        response = self.client.post(
            "/api/recommend-box/",
            data=json.dumps({
                "order_id": "abc"
            }),
            content_type="application/json",
        )

        self.assertEqual(
            response.status_code,
            400
        )