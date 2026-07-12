print("=" * 40)
print("      EXPENSE TRACKER")
print("=" * 40)

expenses = []
total = 0

while True:
    expense = float(input("Enter Expense (Rs.): "))

    expenses.append(expense)
    total += expense

    choice = input("Add another expense? (y/n): ").lower()

    if choice == 'n':
        break

print("\nExpense List")

for i, amount in enumerate(expenses, start=1):
    print(f"{i}. Rs. {amount:.2f}")

print("-" * 40)
print(f"Total Expenses : Rs. {total:.2f}")
print(f"Number of Expenses : {len(expenses)}")
print(f"Average Expense : Rs. {total/len(expenses):.2f}")
print("=" * 40)