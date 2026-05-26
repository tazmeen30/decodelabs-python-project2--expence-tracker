expences = []
total=0
def add_expence():
    global total
    while True:
        amount = input("Enter expence (or 'quit' to stop):")

    #CHECK 1 - empty input
        if amount.strip() =="":
            print("please enter an amount!")
            continue

    #CHECK 2 - quit command
        if amount == "quit":
            break

    #CHECK 3 - safe to convert NOW
        try:
            value= int(amount)
            expences.append(value)
            total += value
            print(f"Added ! Running total: RS. {total}")
        except ValueError:
            print("Invalid! Please enter a number!")
            continue
def view_summary():
    if len(expences) == 0:
        print("no expences added yet!")
    else:
        print("\n" + "=" *30)
        print("      EXPENCE SUMMARY")
        print("=" *30)
        for number , expence in enumerate(expences, start=1):
            print(f" {number}. Rs. {expence}")
        print("-" *30)
        print(f" Total spent: Rs. {total}")
        print("=" *30)
def main():
    print("=" * 30)
    print(" DECODELABS EXPENCE TRACKER")
    print("=" * 30)

    while True:
        print("\nWhat do you want to do?")
        print("1. Add expence")
        print("2. View summary")
        print("3. Exit")
        choice = input("\nEnter choice (1/2/3):")

        if choice =="1":
            add_expence()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            print(f"\nTotal expences recorded: {len(expences)}")
            print(f"Total amount spent: Rs.{total}")
            break
        else:
            print("Invalid choice! Enter 1,2 or 3")

if __name__ == "__main__":
    main()

    

print(f"Total spent : Rs. {total}")


