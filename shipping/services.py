from dataclasses import dataclass
from decimal import Decimal
from itertools import permutations

from .models import Box, Order


@dataclass(frozen=True)
class Recommendation:
    box: Box
    total_weight_kg: Decimal
    total_volume_cm3: Decimal


def dimensions_fit(
    item_dimensions,
    box_dimensions
):
    """
    Check whether an item fits inside a box.

    Rotation is allowed, so all possible
    orientations are checked.
    """

    return any(
        all(
            item <= container
            for item, container
            in zip(item_dimensions, rotation)
        )
        for rotation in permutations(box_dimensions)
    )


def recommend_box(order):
    """
    Find the cheapest box that can contain
    the order according to:

    1. Weight limit
    2. Total volume
    3. Individual product dimensions
    """

    items = list(
        order.items.select_related("product")
    )

    if not items:
        raise ValueError(
            "Order has no items."
        )

    # Calculate total order weight
    total_weight = sum(
        (
            item.product.weight_kg
            * item.quantity
            for item in items
        ),
        Decimal("0"),
    )

    # Calculate total order volume
    total_volume = sum(
        (
            item.product.volume_cm3
            * item.quantity
            for item in items
        ),
        Decimal("0"),
    )

    candidates = []

    for box in Box.objects.all():

        # Check maximum weight
        if total_weight > box.max_weight_kg:
            continue

        # Check total volume
        if total_volume > box.volume_cm3:
            continue

        # Check every product's dimensions
        all_products_fit = all(
            dimensions_fit(
                (
                    item.product.length_cm,
                    item.product.width_cm,
                    item.product.height_cm,
                ),
                (
                    box.internal_length_cm,
                    box.internal_width_cm,
                    box.internal_height_cm,
                ),
            )
            for item in items
        )

        if all_products_fit:
            candidates.append(box)

    if not candidates:
        raise ValueError(
            "No suitable box found for this order."
        )

    # Cheapest suitable box
    box = min(
        candidates,
        key=lambda candidate: (
            candidate.cost,
            candidate.id
        )
    )

    return Recommendation(
        box=box,
        total_weight_kg=total_weight,
        total_volume_cm3=total_volume,
    )