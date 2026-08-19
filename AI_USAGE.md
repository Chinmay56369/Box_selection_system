# AI Usage

## 1. AI Tool Used

I used **ChatGPT** as an AI assistance tool during the development of this Django assignment.

The AI was mainly used for:

* Understanding the assignment requirements.
* Designing the Django project structure.
* Discussing the database models.
* Developing the box recommendation logic.
* Creating Django API code.
* Creating test cases.
* Troubleshooting errors encountered during Postman API testing.
* Reviewing implementation issues and improving the code.

## 2. Prompts Used

The following are examples of the prompts I used during development:

### Prompt 1 — Assignment understanding

I provided the Python/Django hiring assignment and asked for a proper step-by-step implementation.

### Prompt 2 — Project implementation

I asked for the Django project code and a step-by-step process for implementing the box selection system.

### Prompt 3 — Postman testing

I asked how to test the recommendation API using Postman.

### Prompt 4 — Troubleshooting

I provided a screenshot showing a `403 Forbidden` response from Postman and asked for help resolving the issue.

### Prompt 5 — Server error troubleshooting

I provided a screenshot showing a `500 Internal Server Error` / `AttributeError` and asked for help identifying and fixing the problem.

## 3. Output Accepted

I used AI suggestions for parts of the implementation including:

* Django project structure.
* Product, Box, Order and OrderItem models.
* Box recommendation service.
* Dimension rotation checking.
* Weight and volume validation.
* Django API endpoint.
* Django test cases.
* Django Admin configuration.
* GitHub Actions test workflow.
* README structure.
* Postman testing procedure.

The recommendation logic was implemented to:

1. Calculate the total order weight.
2. Calculate the total order volume.
3. Check the box maximum weight.
4. Check the box internal volume.
5. Check whether each product's dimensions fit inside the box.
6. Allow product rotation when checking dimensions.
7. Select the lowest-cost suitable box.

## 4. Output Rejected or Modified

I did not blindly accept all AI-generated code.

During Postman testing, the API initially returned:

```text
403 Forbidden
```

The endpoint was protected by Django CSRF middleware. For the assignment's simple Postman API testing setup, the endpoint was changed to use `@csrf_exempt`.

A second issue appeared after that change:

```text
500 Internal Server Error
AttributeError
```

The problem was a naming conflict between the API view function `recommend_box` and the imported service function with the same name.

The import was therefore changed from:

```python
from .services import recommend_box
```

to:

```python
from .services import recommend_box as get_box_recommendation
```

and the service was called using:

```python
result = get_box_recommendation(order)
```

## 5. Mistakes Identified

### Mistake 1 — CSRF protection during Postman testing

The initial POST request returned:

```text
403 Forbidden
```

This showed that Django's CSRF middleware was rejecting the request from Postman.

The API endpoint was modified for the assignment testing setup.

### Mistake 2 — Function name collision

The view and service were both named:

```python
recommend_box
```

This caused the API view to call the wrong function and resulted in an `AttributeError`.

The service function was aliased as:

```python
get_box_recommendation
```

to make the two responsibilities clear.

## 6. Verification Steps

The implementation was verified progressively by:

* Reviewing the Django project structure.
* Running Django migrations.
* Creating sample Products, Boxes and Orders through Django Admin.
* Starting the Django development server.
* Sending POST requests through Postman.
* Investigating the `403 Forbidden` response.
* Investigating the subsequent `500 Internal Server Error`.
* Correcting the function naming conflict.
* Testing valid and invalid API requests.
* Preparing automated Django test cases.
* Reviewing the recommendation logic against the assignment requirements.

The final submission should only claim tests as passed after they have actually been executed locally or through GitHub Actions.

## 7. Human Review

AI assistance was used as a development aid, but the implementation should be personally reviewed before submission.

In particular, I reviewed:

* The data model.
* Box selection logic.
* API request/response format.
* Error handling.
* Test cases.
* Postman behavior.
* Assignment assumptions.
