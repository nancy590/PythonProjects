# EXPENSE TRACKER

import csv
from datetime import datetime

FILENAME = "expenses.csv"

def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    item = input("Enter item name: ")
    amount = float(input("Enter amount spent: "))
    category = input("Enter category (food, travel, shopping, etc.): ")

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, item, amount, category])

    print("✅ Expense added successfully!\n")

def view_expenses():
    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            print("\nDate        | Item        | Amount | Category")
            print("---------------------------------------------")
            for row in reader:
                print(f"{row[0]:<12} | {row[1]:<10} | {row[2]:<6} | {row[3]}")
    except FileNotFoundError:
        print("⚠️ No expenses found. Add some first!\n")

def total_expenses():
    total = 0
    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                total += float(row[2])
        print(f"\n💰 Total Expenses = {total}\n")
    except FileNotFoundError:
        print("⚠️ No expenses found. Add some first!\n")

def menu():
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break   
        else:
            print("❌ Invalid choice, try again!")

menu()
