# CHAT TRANSCRIPT

## Python/Django Developer Assignment

**AI Tool Used:** ChatGPT  
**Project:** Python/Django Box Selection System  
**Purpose:** Development assistance, implementation guidance, debugging, and API testing.

---

## Conversation 1 — Understanding the Assignment

### User

We operate an ecommerce platform. When a customer places an order, the warehouse team
needs to know which shipping box should be used. Each product has dimensions and
weight. Each box has internal dimensions, maximum weight capacity, and cost.
Your task is to design and build a small Django-based system that recommends the most
suitable box for an order.

give me some idea about the assignment
### ChatGPT

The assignment was broken down into a step-by-step Django development process:

1. Create a Django project.
2. Create the application.
3. Configure the database.
4. Create Product, Box, Order and OrderItem models.
5. Implement the box recommendation algorithm.
6. Create the API endpoint.
7. Configure Django Admin.
8. Create automated tests.
9. Test the API using Postman.
10. Prepare documentation.
11. Configure GitHub Actions.
12. Push the project to GitHub.
13. Prepare the final submission ZIP.

---

# Conversation 2 — Django Project Setup

### User

Give me the code step by step.

### Chatgpt

The project was started with a Python virtual environment.

```bash
mkdir box_selection_system
cd box_selection_system
python -m venv venv

# Conversation 3
### User 
Give me project structure


### Chatgpt

box_selection_system/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── box_selection/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── shipping/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── services.py
│   ├── tests.py
│   └── views.py
│
├── AI_USAGE.md
├── CHAT_TRANSCRIPT.md
├── LEARNINGS.md
├── README.md
├── TEST_CASES.md
├── TEST_OUTPUT.md
├── manage.py
└── requirements.txt

# Conversation 4
### User - It is showing error

User

I uploaded a screenshot of my Postman request.

The screenshot showed a:

403 Forbidden

response.

ChatGPT

The response was identified as a Django CSRF protection issue.

For the API testing setup, the endpoint was changed to use Django's CSRF exemption decorator:

from django.views.decorators.csrf import csrf_exempt

The view was decorated with:

@csrf_exempt
@require_POST
def recommend_box(request):

The file was saved and the Postman request was tested again.

18. Second Postman Error — 500 Internal Server Error
User

I uploaded another screenshot.

The screenshot showed:

500 Internal Server Error

with an AttributeError.

ChatGPT

The issue was identified as a naming conflict.

The API view was called:

recommend_box

and the service function was also imported as:

recommend_box

This created a conflict in the view module.

The import was changed from:

from .services import recommend_box

to:from .services import recommend_box as get_box_recommendation


# conversation 5
###User- give me idea about readme.md file

### chatgpt

The README should explain:

Project overview.
Technologies used.
Installation.
Database setup.
How to run the server.
API usage.
Recommendation algorithm.
Assumptions.
Testing.
Project structure.