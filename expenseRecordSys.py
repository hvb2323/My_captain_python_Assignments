import json
import os
from datetime import datetime
import matplotlib.pyplot as plt

#Creating a file for storing the data
#lets create a file called "Expense_file"
Expense_file="expense_data.json"

#creating a fuction for loading the data from the file"Expense_file"
def load():
  if os.path.exists(Expense_file):
    with open(Expense_file,'r') as file:
      return json.load(file)
  else:
    return{"expenses":[]}

#creating a function called save for saving the data into the file
def save(data):
  with open(Expense_file,'w') as file:
    json.dump(data,file,indent=2)


#creating function called add for entering the new entries
def add():
  amount=float(input("enter the amount spent:"))
  category=input("enter the category /add a new category")
#if already there exists a category data we dont need to enter a new entry inplaceof we are going to load existing data
  expense_data=load()

#for add new entry
  expense={
      "amount":amount,
      "category":category,
      "date":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  }
  expense_data["expenses"].append(expense)

#saving the updated data
  save(expense_data)
  print("expenses recorde successfull")

#displaying the entries
def show_summ():
    expense_data=load()

    if not expense_data["expenses"]:
      print("not yet recorded")
      return
    total=sum(expense['amount'] for expense in expense_data['expenses'])
    print(f"total amount spent:{total:.2f}/-")

#displaying by categories
    categories = {}
    for expense in expense_data["expenses"]:
        category = expense['category']
        categories[category] = categories.get(category, 0) + expense['amount']

    print("Breakdown by categories:")
    for category, amount in categories.items():
        print(f"{category}: {amount:.2f}/-")

    # : Display a pie chart of expenses
    labels = categories.keys()
    values = categories.values()

    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title("Expense Breakdown by Categories")
    plt.show()
def main():
    while True:
        print("\nExpense Recording System")
        print("1. Add Expense")
        print("2. Show Summary")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            add()
        elif choice == "2":
            show_summ()
        elif choice == "3":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

main()

              
