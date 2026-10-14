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
    ├── main.py         # Entry point: order calculator CLI
    └── calculator.py   # calculate_total() and get_grade()
```

## Day 1: Python Fundamentals + Docker

- `calculate_total(price, quantity, discount=0)` returns the order total after a percentage discount. It rejects a negative price, a negative quantity, and a discount outside 0–100.
- `get_grade(score)` returns a letter grade from A to F. It rejects scores outside 0–100.
- `main.py` prints an order summary for each hard-coded sample product.
