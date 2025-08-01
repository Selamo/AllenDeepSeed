import datetime
import json
import os

# === CONFIG ===
DATA_FILE = "budget_data.json"
BUDGET_LIMITS = {
    "food": 400,
    "transport": 150,
    "housing": 800,
    "entertainment": 200
}

# === UTILITIES ===
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def validate_date(date_str):
    try:
        datetime.datetime.strptime(date_str, "%Y-%m")
        return True
    except ValueError:
        return False

def format_currency(amount):
    return f"${amount:,.2f}"

def print_bar_chart(category_data, total):
    for cat, amt in category_data.items():
        percent = (amt / total) * 100 if total else 0
        bars = "█" * int(percent // 5)
        print(f"{cat.capitalize():<12} {bars:<20} {format_currency(amt)} ({percent:.1f}%)")

def budget_warnings(expenses):
    for cat, spent in expenses.items():
        limit = BUDGET_LIMITS.get(cat, None)
        if limit and spent > limit:
            over = spent - limit
            percent = (spent / limit) * 100
            print(f"{cat.capitalize()}: {format_currency(over)} over budget ({percent:.1f}% of limit)")

# === MAIN FUNCTIONS ===
def add_transaction(data):
    date = input("Enter month (YYYY-MM): ")
    if not validate_date(date):
        print(" Invalid date format!")
        return

    t_type = input("Type (income/expense): ").strip().lower()
    if t_type not in ["income", "expense"]:
        print(" Must be 'income' or 'expense'")
        return

    category = input("Category: ").strip().lower()
    amount = float(input("Amount: $"))

    data.setdefault(date, {"income": {}, "expenses": {}})
    section = "income" if t_type == "income" else "expenses"
    data[date][section][category] = data[date][section].get(category, 0) + amount
    save_data(data)
    print(" Transaction added!")

def view_summary(data):
    date = input("Enter month (YYYY-MM): ")
    if date not in data:
        print(" No data for that month.")
        return

    month_data = data[date]
    incomes = month_data.get("income", {})
    expenses = month_data.get("expenses", {})

    total_income = sum(incomes.values())
    total_expense = sum(expenses.values())
    net = total_income - total_expense
    net_percent = (net / total_income) * 100 if total_income else 0

    print(f"\n=== FINANCIAL SUMMARY for {date} ===")
    print(f" Total Income:   {format_currency(total_income)}")
    print(f" Total Expenses: {format_currency(total_expense)}")
    print(f" Net Savings:    {format_currency(net)} ({net_percent:.1f}%)")

    print("\n EXPENSE BREAKDOWN")
    print_bar_chart(expenses, total_expense)

    print("\n BUDGET ALERTS:")
    budget_warnings(expenses)

def export_summary(data):
    date = input("Enter month to export (YYYY-MM): ")
    if date not in data:
        print(" No data for that month.")
        return

    filename = f"summary_{date}.txt"
    month_data = data[date]
    incomes = month_data.get("income", {})
    expenses = month_data.get("expenses", {})

    total_income = sum(incomes.values())
    total_expense = sum(expenses.values())
    net = total_income - total_expense

    with open(filename, "w") as f:
        f.write(f"=== Budget Summary for {date} ===\n")
        f.write(f"Total Income: {format_currency(total_income)}\n")
        f.write(f"Total Expenses: {format_currency(total_expense)}\n")
        f.write(f"Net Savings: {format_currency(net)}\n\n")
        f.write("Expense Breakdown:\n")
        for cat, amt in expenses.items():
            percent = (amt / total_expense) * 100 if total_expense else 0
            f.write(f"- {cat.capitalize()}: {format_currency(amt)} ({percent:.1f}%)\n")

    print(f" Exported to {filename}")
data = load_data()
while True:
        
      print("\n=== PERSONAL BUDGET TRACKER ===")
      print("1. Add Income/Expense")
      print("2. View Monthly Summary")
      print("3. Export Summary")
      print("4. Exit")

      choice = input("Choose an option: ").strip()

      if choice == "1":
         add_transaction(data)
      elif choice == "2":
            view_summary(data)
      elif choice == "3":
            export_summary(data)
      elif choice == "4":
            print(" Exiting...")
            break
      else:
            print("Invalid choice!")
    



 
