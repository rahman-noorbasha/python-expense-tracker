import json
expenses=[]
def add_expenses():
    name = input("Enter expense name:")
    amount = float(input("Enter expense amount:"))
    expense={
        "name":name,
        "amount":amount
    }
    expenses.append(expense)
    print("Expense added successfully")
def  view_expenses():
    if len(expenses)==0:
        print("No Expenses found")
    else:
        print("\n===== Expenses =====")
        for expense in expenses:
            print(expense["name"],"-",expense["amount"])
def search_expenses():

    search_name = input("Enter expense name to search: ")

    for expense in expenses:

        if expense["name"].lower() == search_name.lower():
            print(expense["name"],"-",expense["amount"])
            return

    print("expense not found")
def delete_expense():

    delete_name = input("Enter expense name to delete: ")

    for expense in expenses:

        if expense["name"].lower() == delete_name.lower():
            expenses.remove(expense)
            print("Expense deleted successfully")
            return

    print("expense not found")
def save_expenses():
        file=open("expenses.txt","w")
        for expense in expenses:
            file.write(expense["name"]+","+str(expense["amount"])+"\n")
        file.close()
def load_expenses():
        try:

            file=open("expenses.txt","r")
            for line in file:
                name, amount= line.strip().split(",")
                expenses.append({
                    "name":name,
                    "amount":amount
                })
            file.close()
        except FileNotFoundError:
            pass
load_expenses()

while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4.Delete Expense")
    print("5. Exit")
    choice= input("enter your choice:")
    if choice == "1":
        add_expenses()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        search_expenses()
    elif choice == "4":
        delete_expense()
    elif choice == "5":
        save_expenses()
        print("Data saved")
        print("Exiting...")
        break
    else:
        print("Invalid choice")