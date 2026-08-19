# LEARNINGS

## Python/Django Box Selection System

This document summarizes the technical concepts, practical lessons, debugging experience, and development practices learned while implementing the Python/Django Box Selection System.

---

## 1. Django Project Structure

One of the first things I learned was how a Django project is organized.

The project contains:

- A Django project configuration.
- A Django application containing the business functionality.
- Models for database entities.
- Views for handling HTTP requests.
- Services for business logic.
- Tests for automated verification.
- Admin configuration for managing database records.

A simplified structure is:

```text
box_selection_system/
│
├── box_selection/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── shipping/
│   ├── models.py
│   ├── services.py
│   ├── views.py
│   ├── admin.py
│   └── tests.py
│
├── manage.py
└── requirements.txt

###  LEARNINGS -

1.Keeping the business logic separate from the API view makes the application easier to understand, test, and maintain.
2.Database relationships should represent the actual business requirements instead of putting everything into one model.
Using separate models also makes the application easier to extend later.
3.When working with physical dimensions, orientation matters.
The implementation therefore checks different permutations of the product dimensions rather than assuming that length must always match length.
4.Business rules often require multiple conditions to be satisfied simultaneously.
A box must satisfy the weight requirement as well as the physical size requirements.
5.Filtering and sorting are useful when implementing selection-based business logic.
It is important to first verify that a box is valid and only then compare its cost.
6.The view should mainly handle:

Receiving the request.
Validating input.
Finding the relevant order.
Calling the service.
Returning the response.

The service should handle the actual box recommendation logic.

This makes the business logic easier to test independently.
7.This assignment helped me gain practical experience with Django beyond basic CRUD operations.

The most useful part was connecting several concepts into one working application:
Database
   ↓
Django Models
   ↓
Business Logic
   ↓
API
   ↓
Postman
   ↓
Automated Tests
   ↓
GitHub
   ↓
CI/CD