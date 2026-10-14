# Python FastAPI Training

A 2-week Python and FastAPI training program. Everything runs through Docker, so you don't need Python installed locally.

## Requirements

- Docker with Docker Compose v2

## How to Run

Build the image (once, or after changing `Dockerfile` or `requirements.txt`):

```bash
docker compose build
```

Run the program:

```bash
docker compose run --rm app python main.py
```

Run the tests:

```bash
docker compose run --rm app pytest -v
```

Check the Python version inside the container:

```bash
docker compose run --rm app python --version
```

## Project Structure

```text
.
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── app/
    ├── main.py                     # Entry point: wires the loader and service together
    ├── calculator.py               # Day 1: calculate_total() and get_grade()
    ├── data/
    │   ├── products.json           # Sample product data
    │   └── report.json             # Day 2: generated summary report
    ├── models/
    │   └── product.py              # Product dataclass
    ├── services/
    │   ├── product_loader.py       # Loads products.json into Product objects
    │   └── product_service.py      # ProductService business logic, ProductNotFoundError
    └── tests/
        └── test_product_service.py # Pytest suite
```

## Day 1: Python Fundamentals + Docker

- `calculate_total(price, quantity, discount=0)` returns the order total after a percentage discount. It rejects a negative price, a negative quantity, and a discount outside 0–100.
- `get_grade(score)` returns a letter grade from A to F. It rejects scores outside 0–100.

## Day 2: Collections, JSON, Files, and Exceptions

- Loaded product data from JSON, with handling for a missing file and invalid JSON.
- Filtered and transformed data with list and set comprehensions.
- Generated a summary report and wrote it to `app/data/report.json`.
- Added a custom `ProductNotFoundError` exception.

The Day 2 code was refactored into `models/` and `services/` on Day 3.

## Day 3: Dataclasses, Services, and Pytest

- `Product` is a dataclass. Its `is_available` property returns `True` when stock is greater than 0.
- `load_products(filename)` reads JSON and returns a list of `Product` objects. It returns `[]` when the file is missing or invalid.
- `ProductService` receives a list of products, so it never reads files itself. This keeps data loading separate from business logic and makes the service easy to test. It provides:
  - `get_available()` returns the products that are in stock.
  - `find(product_id)` returns the matching product, or raises `ProductNotFoundError`.
  - `inventory_value()` returns the sum of price × stock across all products.
- The tests use pytest fixtures (`products`, `service`) for shared test data. They cover happy paths, failure paths, and empty-list edge cases.
