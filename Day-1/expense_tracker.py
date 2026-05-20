import json #to read/write json file
import os #to check if file exists or not
from datetime import date

FILENAME = "expenses.json"


def load_expenses():
    if os.path.exists(FILENAME):        
        with open(FILENAME, "r") as f: 
            return json.load(f)  #file to python
    return []                


def save_expenses(expenses):
    with open(FILENAME, "w") as f:
        json.dump(expenses, f, indent=4)  #python to file


def add_expense(amount, category, description):
    # Input validation
    if amount <= 0:
        print("Amount must be greater than 0")
        return
    if not category.strip():
        print("Category cannot be empty")
        return
    if not description.strip():
        print("Description cannot be empty!")
        return
    
    expenses = load_expenses()       
    new_expense = {
        "id": len(expenses) + 1,      
        "amount": amount,          
        "category": category.lower(),  #always lowercase
        "description": description,     
        "date": str(date.today())
    }
    expenses.append(new_expense)  
    save_expenses(expenses)              
    print(f"Expense added!")


def list_expenses():
    expenses = load_expenses()
    if len(expenses) == 0:     
        print("No expenses found!")
    else:
        for expense in expenses:      
            print(f"[{expense['id']}] {expense['category']} | ₹{expense['amount']} | {expense['description']} | {expense['date']}")
        total = sum(e["amount"] for e in expenses)
        print(f"\nTotal: ₹{total:.2f} ({len(expenses)} expenses)")


def filter_by_category(category):
    expenses = load_expenses()
    found = False
    for expense in expenses:
        if expense["category"] == category.lower():
            print(f"[{expense['id']}] ₹{expense['amount']} | {expense['description']} | {expense['date']}")
            found = True
    if not found:
        print("No expenses in this category!")


def delete_expense(expense_id):
    expenses = load_expenses()
    original_length = len(expenses)
    expenses = [e for e in expenses if e["id"] != expense_id]
    if len(expenses) == original_length:
        print(f"No expense found with ID {expense_id}!")
        return
    save_expenses(expenses)
    print(f"Expense {expense_id} deleted!")


def summarise():
    expenses = load_expenses()
    if len(expenses) == 0:
        print("No Expenses Found")
        return
    totals = {}
    for expense in expenses:
        category = expense["category"]
        if category not in totals:
            totals[category] = 0
        totals[category] += expense["amount"]
    print("\nSUMMARY----")
    for category, total in totals.items():
        print(f"{category:15} → ₹{total:.2f}")
    print(f"\nGrand Total    → ₹{sum(totals.values()):.2f}")


def main():
    while True:
        print("\n-Expense Tracker----")
        print("1. Add Expense")
        print("2. List Expenses")
        print("3. Filter by Category")
        print("4. Summarise")
        print("5. Delete Expense")
        print("6. Quit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            try:
                amount = float(input("Amount: "))
            except ValueError:
                print("Invalid amount! Enter a number.")
                continue
            category = input("Category: ").strip().lower()
            description = input("Description: ").strip()
            add_expense(amount, category, description)

        elif choice == "2":
            list_expenses()

        elif choice == "3":
            category = input("Category: ").strip().lower()
            filter_by_category(category)

        elif choice == "4":
            summarise()

        elif choice == "5":
            try:
                expense_id = int(input("Enter expense ID to delete: "))
                delete_expense(expense_id)
            except ValueError:
                print("Invalid ID!")

        elif choice == "6":
            print("Bye!")
            break

        else:
            print("Invalid choice!")

main()