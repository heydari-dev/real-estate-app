# Real Estate CLI System

A lightweight real estate management system built with pure Python using advanced Object-Oriented Programming concepts.

This project simulates a property advertisement platform and demonstrates how a simple ORM-like structure can be implemented without external frameworks.

---

## Key Features

- Object-Oriented Architecture
- Custom Manager (Mini ORM style)
- Multiple Inheritance
- Sell Advertisement System
- Dynamic Object Storage
- CLI Interaction

---

## Architecture Overview

- `BaseClass` → Handles ID generation & object storage
- `Manager` → Provides search, get, count methods
- `Estate` types → Apartment, House, Store
- `Advertisement` types → Sell (Rent structure prepared)

Example usage:

```python
ApartmentSell.manager.search(area__min=70)
```

---

## Run Project

```bash
git clone https://github.com/heydari-dev/real-estate-app.git
cd real-estate-app
python main.py
```
