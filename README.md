# AI-Assisted Box Selection System

A small Django application for recommending a shipping box for an ecommerce order.

## Assignment interpretation

The assignment says that products have dimensions and weight, while boxes have internal dimensions, maximum weight and cost. The system should recommend a suitable box. The assignment does not define an exact 3D packing algorithm, API shape, authentication requirement, database engine, or UI.

This implementation therefore makes the following explicit assumptions:

1. One order is packed into one box.
2. The total weight must be within the box's maximum weight.
3. The total product volume must be within the box's internal volume.
4. Every individual product must fit inside the box in at least one rotation.
5. The recommended box is the lowest-cost box satisfying all checks.
6. Exact 3D placement of multiple products is outside this small assignment; volume is used as an approximation. A production implementation should replace this with a true 3D packing algorithm if exact placement is required.

## Tech stack

- Python
- Django
- SQLite for local development/testing
- Django TestCase
- GitHub Actions

## Project structure

```text
box_selection_system/
├── box_selection/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── shipping/
│   ├── admin.py
│   ├── models.py
│   ├── services.py
│   ├── tests.py
│   └── views.py
├── .github/workflows/tests.yml
├── AI_USAGE.md
├── CHAT_TRANSCRIPT.md
├── LEARNINGS.md
├── TEST_CASES.md
├── TEST_OUTPUT.md
├── manage.py
└── requirements.txt
```

## Setup

Python 3.11+ is recommended.

### 1. Create and activate a virtual environment

Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create the database

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Run tests

```bash
python manage.py test
```

### 5. Run the server

```bash
python manage.py runserver
```

## API

Endpoint:

```text
POST /api/recommend-box/
```

Request:

```json
{
  "order_id": 1
}
```

Example successful response:

```json
{
  "order_id": 1,
  "recommended_box": {
    "id": 1,
    "name": "Small",
    "cost": "3.00"
  },
  "total_weight_kg": "1.000",
  "total_volume_cm3": "1000.00"
}
```

## Creating sample data

Use Django admin at `/admin/` or the Django shell:

```bash
python manage.py shell
```

Then create products, boxes, orders and order items using the models in `shipping/models.py`.

## Verification

The test suite covers:

- dimension rotation
- lowest-cost suitable box
- weight limit
- no suitable box
- empty order
- API success
- API validation

Before submission, run:

```bash
python manage.py test
```

Copy the actual terminal output into `TEST_OUTPUT.md`, or use the GitHub Actions workflow.

## Submission checklist

Before creating the ZIP, the candidate should personally:

- [ ] Create the GitHub repository and push the project.
- [ ] Replace the placeholder in `CHAT_TRANSCRIPT.md` with the candidate's own exported chat transcript.
- [ ] Write `LEARNINGS.md` personally. The assignment explicitly says AI must not generate this answer.
- [ ] Update `AI_USAGE.md` so it accurately reflects the AI tools, prompts, accepted/rejected outputs, mistakes, and verification actually used.
- [ ] Run the test suite and paste the real output into `TEST_OUTPUT.md`.
- [ ] Add the real GitHub repository link to the final submission email.
- [ ] Create one ZIP containing the repository files.

Do not claim that a test, GitHub Action, transcript export, or manual verification was completed unless it was actually completed.
