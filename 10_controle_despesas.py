expenses = []

def add_expense(description, amount):
    expenses.append((description, amount))

def calculate_balance():
    return sum(amount for description, amount in expenses)

def view_expenses():
    for description, amount in expenses:
        print(f"{description}: ${amount:.2f}")

# Example usage
add_expense("Rent", 500)
add_expense("Groceries", 150)
view_expenses()
print(f"Total balance: ${calculate_balance():.2f}")
