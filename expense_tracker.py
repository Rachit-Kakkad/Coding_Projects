expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount (in Rs.): "))
    category = input("Enter category (e.g., Food, Travel, Shopping, etc.): ")
    date = input("Enter date (DD-MM-YYYY): ")

    expense = {
        "name": name,
        "amount": amount,
        "category": category,
        "date": date
    }

    expenses.append(expense)
    print("✅ Expense added successfully!\n")

def view_expense():
    if not expenses:
        print("🚫 No expenses added yet! Please add some expenses first.\n")
        return

    print("------- ALL EXPENSES -------")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['date']} | {expense['name']} | {expense['category']} | Rs. {expense['amount']}")
    print()  # For spacing

def total_spent():
    total = sum(exp['amount'] for exp in expenses)
    print(f"💰 Your Total Expense is: Rs. {total}\n")

def run_tracker():
    your_name = input("Enter Your Name: ")
    your_prefix = input("Enter your prefix { Mr. / Mrs. }: ")

    print(f"\nWelcome {your_prefix} {your_name},")
    print("You're heartily welcomed to our 'Expense Tracker App'!\n")

    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Spent")
        print("4. Exit\n")

        option = input("👉 Select an option (1 to 4): ")

        if option == "1":
            add_expense()
        elif option == "2":
            view_expense()
        elif option == "3":
            total_spent()
        elif option == "4":
            print("👋 Exiting the Expense Tracker App. Bye-bye!\n")
            break
        else:
            print("❌ Invalid option! Please choose between 1 and 4.\n")

# Run the app
run_tracker()
