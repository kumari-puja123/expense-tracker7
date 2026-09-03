#Expenses Tracker project
#-Tracker/
# expense_tracker.py
expenses=[] #list of expenses in form of dictionary
print("welcome to Expense Tracker")

while True:
    print("=====MENU=====")
    print("1. Add Expense ")
    print("2.view All Expenses")
    print("3. view TOtal Amount")
    print("4. Exit")

    choice= input("please Enter Your Choice:")

    #Add Expense
    if(choice =="1"):
        date=input("Enter the date of expense")
        category=input("Enter the expense category(food,travel,makeup,books):")
        description=input("Enter a short description:")
        amount=float(input("enter the amount:"))

        expense={
            "date":date,
            "category":category,
            "description":description,
            "amount":amount
        }

        expenses.append(expense)
        print("\nexpense added successfully")

    #2.view ALL EXPENSES
    elif (choice=="2"):
        if (len(expenses)==0):
            print("No Expenses Added.please add an expense first.")
        else:
            print("===== All Your Expenses =====")
            count=1
            for eachExpense in expenses:
                print(f"Expense No.{count}->{eachExpense['date']},{eachExpense['category']},{eachExpense['description']},Amount:{eachExpense['amount']}")
                count=count+1

    #view Total Spending
    elif (choice=="3"):
        total=0
        for eachExpense in expenses:
            total=total+eachExpense["amount"]
        print("\n TOTAL EXPENSE = ", total)

    #4.exit
    elif choice=="4":
        print("Thank you for using our system")
        break
    else:
        print("Invalid choice")
