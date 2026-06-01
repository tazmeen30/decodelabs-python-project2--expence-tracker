# ==========================================
# Project: Expense Tracker
# Developed by: Tazmeen Iram
# Internship Project - DecodeLabs
# ==========================================

# List to store all expenses entered by the user
expenses = []

# Variable to keep track of the total amount spent
total = 0


def add_expense():
    """
    Function to add expenses.

    The user can continuously enter expense amounts.
    Typing 'quit' stops expense entry and returns to the main menu.
    Input validation ensures only valid numeric values are accepted.
    """

    global total

    while True:
        # Take expense input from the user
        amount = input("Enter expense (or 'quit' to stop): ")

        # Check 1: Empty input validation
        if amount.strip() == "":
            print("Please enter an amount!")
            continue

        # Check 2: Stop adding expenses
        if amount == "quit":
            break

        # Check 3: Convert input to a number safely
        try:
            value = int(amount)

            # Store expense in the list
            expenses.append(value)

            # Update running total
            total += value

            print(f"Added! Running total: Rs. {total}")

        except ValueError:
            # Handle non-numeric input
            print("Invalid! Please enter a number!")
            continue


def view_summary():
    """
    Function to display all recorded expenses
    along with the total amount spent.
    """

    # Check if any expenses have been added
    if len(expenses) == 0:
        print("No expenses added yet!")

    else:
        print("\n" + "=" * 30)
        print("      EXPENSE SUMMARY")
        print("=" * 30)

        # Display expenses with numbering
        for number, expense in enumerate(expenses, start=1):
            print(f"{number}. Rs. {expense}")

        print("-" * 30)

        # Display total spending
        print(f"Total spent: Rs. {total}")

        print("=" * 30)


def main():
    """
    Main function that controls the menu-driven interface.

    Features:
    1. Add expenses
    2. View expense summary
    3. Exit the application
    """

    # Application header
    print("=" * 30)
    print(" DECODELABS EXPENSE TRACKER ")
    print("=" * 30)

    while True:

        # Display menu options
        print("\nWhat do you want to do?")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")

        # Take user choice
        choice = input("\nEnter choice (1/2/3): ")

        # Add expenses
        if choice == "1":
            add_expense()

        # View summary
        elif choice == "2":
            view_summary()

        # Exit program
        elif choice == "3":
            print(f"\nTotal expenses recorded: {len(expenses)}")
            print(f"Total amount spent: Rs. {total}")
            break

        # Handle invalid choices
        else:
            print("Invalid choice! Enter 1, 2 or 3.")


# Program execution starts here
if __name__ == "__main__":
    main()

# Display final total spent
print(f"Total spent: Rs. {total}")
