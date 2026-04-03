# Grocery Store Management System

A hype-ready Python grocery bro app with CLI and GUI modes for inventory, customer leads, and revenue tracking.

## Features

- **Add Products** — Add items with name, price, and quantity to inventory
- **Update Stock** — Adjust product quantities in real-time
- **Delete Products** — Remove products from inventory
- **Search Items** — Search by product name or ID
- **Manage Customers** — Add and track customer records
- **Process Sales** — Complete transactions with automatic stock updates
- **Billing System** — Generate detailed invoices with total calculations
- **Sales History** — View all completed sales and transactions

## Requirements

- Python 3.9+

## Run - Choose Your Mode

### Option 1: Interactive Mode Selection
```bash
python app.py
```
Then select:
- **1** for CLI (Command-line interface)
- **2** for GUI (Graphical interface)

### Option 2: Direct CLI Mode
```bash
python cli_app.py
```

### Option 3: Direct GUI Mode
```bash
python gui_app.py
```

## Project Structure

- `app.py` - main application with mode selection
- `cli_app.py` - direct CLI entry point
- `gui_app.py` - direct GUI entry point
- `grocery_store/database.py` - SQLite database initialization
- `grocery_store/services.py` - inventory, customer, and sales business logic
- `grocery_store/gui.py` - Tkinter graphical user interface
- `grocery_store/cli.py` - command-line interface
- `data/store.db` - runtime SQLite database file
