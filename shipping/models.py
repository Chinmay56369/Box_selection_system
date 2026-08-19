from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=150)

    length_cm = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    width_cm = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    height_cm = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    weight_kg = models.DecimalField(
        max_digits=8,
        decimal_places=3
    )

    def __str__(self):
        return self.name

    @property
    def volume_cm3(self):
        return (
            self.length_cm
            * self.width_cm
            * self.height_cm
        )


class Box(models.Model):
    name = models.CharField(max_length=100)

    internal_length_cm = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    internal_width_cm = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    internal_height_cm = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    max_weight_kg = models.DecimalField(
        max_digits=8,
        decimal_places=3
    )

    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    class Meta:
        ordering = ["cost", "id"]

    def __str__(self):
        return self.name

    @property
    def volume_cm3(self):
        return (
            self.internal_length_cm
            * self.internal_width_cm
            * self.internal_height_cm
        )


class Order(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Order #{self.pk}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT
    )

    quantity = models.PositiveIntegerField()

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=models.Q(quantity__gt=0),
                name="order_item_quantity_gt_zero",
            )
        ]

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"