import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import Order
from .services import recommend_box as get_box_recommendation


@csrf_exempt
@require_POST
def recommend_box(request):

    try:
        # Read JSON request body
        payload = json.loads(
            request.body or "{}"
        )

        # Get order ID
        order_id = payload.get("order_id")

        # Validate order ID
        if not isinstance(order_id, int):
            return JsonResponse(
                {
                    "error": "order_id must be an integer."
                },
                status=400,
            )

        # Find order
        order = Order.objects.get(
            pk=order_id
        )

        # Get recommended box
        result = get_box_recommendation(order)

        # Return response
        return JsonResponse(
            {
                "order_id": order.id,

                "recommended_box": {
                    "id": result.box.id,
                    "name": result.box.name,
                    "cost": str(result.box.cost),
                },

                "total_weight_kg": str(
                    result.total_weight_kg
                ),

                "total_volume_cm3": str(
                    result.total_volume_cm3
                ),
            }
        )

    except Order.DoesNotExist:

        return JsonResponse(
            {
                "error": "Order not found."
            },
            status=404,
        )

    except ValueError as exc:

        return JsonResponse(
            {
                "error": str(exc)
            },
            status=400,
        )

    except json.JSONDecodeError:

        return JsonResponse(
            {
                "error": "Request body must be valid JSON."
            },
            status=400,
        )