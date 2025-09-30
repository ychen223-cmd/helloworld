import random

# Variables
player_name = input("☕ Welcome to the Cute Coffee Shop! What's your name? ")
total_bill = 0
order_list = []

# Functions
def showMenu():
    print("\n--- Menu ---")
    print("1. Americano - $5 ☕")
    print("2. Latte - $8 🥛")
    print("3. Mocha - $10 🍫")
    print("4. Special Surprise - ??? 🎁")

def checkout(item, price):
    global total_bill
    total_bill += price
    order_list.append(item)
    print(f"\nAdded {item} to your order. 🛒 Current total: ${total_bill}")

def showOrder():
    print("\nYour current order: ", ", ".join(order_list))
    print(f"Total bill so far: ${total_bill}")

# Game Start
print(f"\nHi {player_name}! Welcome to our Cute Coffee Shop! 🐱")

while True:
    showMenu()
    choice = input("Enter the number of the drink you want (or '0' to finish): ")

    if choice == "0":
        break
    elif choice == "1":
        checkout("Americano", 5)
    elif choice == "2":
        checkout("Latte", 8)
    elif choice == "3":
        checkout("Mocha", 10)
    elif choice == "4":
        # Random surprise drink
        surprise_price = random.choice([6, 12, 0])
        surprise_item = random.choice(["Rainbow Latte 🌈", "Magic Mocha ✨", "Free Cookie 🍪"])
        checkout(surprise_item, surprise_price)
        print("Wow! You got a surprise! 🎉")
    else:
        print("Sorry, that option is not on the menu. ❌")

    showOrder()

# Game Ending
print(f"\nThank you for visiting, {player_name}! 🥰")
print(f"Your final order: {', '.join(order_list)}")
print(f"Total amount to pay: ${total_bill}")
print("Have a wonderful day! 🌞")