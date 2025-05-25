import csv
import os

FILENAME = 'expenses.csv'

def init_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Category', 'Amount', 'Note'])

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., food, transport): ")
    amount = input("Enter amount: ")
    note = input("Enter a note (optional): ")

    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, note])
    print("Expense added!")

def view_expenses():
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print('\t'.join(row))

def total_expenses():
    total = 0
    with open(FILENAME, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += float(row['Amount'])
    print(f"Total Expenses: ${total:.2f}")

def menu():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_expenses()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    init_file()
    menu()
