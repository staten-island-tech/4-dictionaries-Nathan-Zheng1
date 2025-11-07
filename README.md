cart = []
items = [
{
    "name" : "Mystery Block",
    "price" : 10,
    "department" : "Mystery",
    "description" : "A mystery block that could contain all the necesities you need: money, coupons, and even a grand prize; a house! Are you willing to take a risk, for a chance at a brand new house? 70% chance for nothing, 25% chance for 1-25 dollars, respectively, ~5% chance for in store coupons and promotions, and a 1/10,000,000 chance for the grand prize!"
},
{
    "name" : "Phone",
    "price" : 999,
    "department" : "Technology",
    "description" : "A absolutely brain metlting device, for all your silly desires."
},
{
    "name" : "PC",
    "price" : 1999,
    "department" : "Technology",
    "description" : "A super power of a device, capable of running all types of games, and the exclusive powerhouse: GPT+"
},
{
    "name" : "IPad",
    "price" : 1250,
    "department" : "Technology",
    "description" : "The bane of all of time, the device that withholds true wisdom, yet such a addicting little device." 
}
]
total = 0
print("Here are all the items we currently have in stock:")
for index, item in enumerate(items):
    print(index, ":" , item["name"])
user_input = input("Would you like to get any of these devices?")
if user_input == "0":
    user_input = input(f"Are you sure you would like to get {items[0]["name"]}.")
    if user_input == "yes":
        print(f"Great! Your total will be {items[0]["price"]} dollars.")
        total += 10
        user_input = input("Would you like to see the description and department?")
        if user_input == "yes":
            print(f"This item is part of the {items[0]["department"]} department, the description is shown as the following: {items[0]["description"]}")
if user_input == "1":
    user_input = input(f"Are you sure you would like to get {items[1]["name"]}.")
    if user_input == "yes":
        print(f"Great! Your total will be {items[1]["price"]} dollars.")
        total += 999
        user_input = input("Would you like to see the description and department?")
        if user_input == "yes":
            print(f"This item is part of the {items[1]["department"]} department, the description is shown as the following: {items[1]["description"]}")
if user_input == "2":
    user_input = input(f"Are you sure you would like to get {items[2]["name"]}.")
    if user_input == "yes":
        print(f"Great! Your total will be {items[2]["price"]} dollars.")
        total += 1999
        user_input = input("Would you like to see the description and department?")
        if user_input == "yes":
            print(f"This item is part of the {items[2]["department"]} department, the description is shown as the following: {items[2]["description"]}")
if user_input == "3":
    user_input = input(f"Are you sure you would like to get {items[3]["name"]}.")
    if user_input == "yes":
        print(f"Great! Your total will be {items[3]["price"]} dollars.")
        total += 1250
        user_input = input("Would you like to see the description and department?")
        if user_input == "yes":
            print(f"This item is part of the {items[3]["department"]} department, the description is shown as the following: {items[3]["description"]}")
user_input = input("Would you like to continue shopping?")
if user_input == "no":
    user_input == input(f"Alright! Your total is ${total} Will you be paying with cash or card?")
if user_input == "cash":
    print("Okay, pay up here.")
elif user_input == "card":
    print("Okay, scan over here.")
elif user_input == "yes":
    for index, item in enumerate(items):
        print(index, ":" , item["name"])
user_input = input("Would you like to get any of these devices?")
if user_input == "0":
    user_input = input(f"Are you sure you would like to get {items[0]["name"]}.")
    if user_input == "yes":
        print(f"Great! Your total will be {items[0]["price"]} dollars.")
        total += 10
        user_input = input("Would you like to see the description and department?")
        if user_input == "yes":
            print(f"This item is part of the {items[0]["department"]} department, the description is shown as the following: {items[0]["description"]}")
if user_input == "1":
    user_input = input(f"Are you sure you would like to get {items[1]["name"]}.")
    if user_input == "yes":
        print(f"Great! Your total will be {items[1]["price"]} dollars.")
        total += 999
        user_input = input("Would you like to see the description and department?")
        if user_input == "yes":
            print(f"This item is part of the {items[1]["department"]} department, the description is shown as the following: {items[1]["description"]}")
if user_input == "2":
    user_input = input(f"Are you sure you would like to get {items[2]["name"]}.")
    if user_input == "yes":
        print(f"Great! Your total will be {items[2]["price"]} dollars.")
        total += 1999
        user_input = input("Would you like to see the description and department?")
        if user_input == "yes":
            print(f"This item is part of the {items[2]["department"]} department, the description is shown as the following: {items[2]["description"]}")
if user_input == "3":
    user_input = input(f"Are you sure you would like to get {items[3]["name"]}.")
    if user_input == "yes":
        print(f"Great! Your total will be {items[3]["price"]} dollars.")
        total += 1250
        user_input = input("Would you like to see the description and department?")
        if user_input == "yes":
            print(f"This item is part of the {items[3]["department"]} department, the description is shown as the following: {items[3]["description"]}")
user_input = input("Would you like to continue shopping?")
if user_input == "no":
    user_input == input(f"Alright! Your total is ${total} Will you be paying with cash or card?")
if user_input == "cash":
    print("Okay, pay up here.")
elif user_input == "card":
    print("Okay, scan over here.")
elif user_input == "yes":
    for index, item in enumerate(items):
        print(index, ":" , item["name"])
user_input = input("Would you like to get any of these devices?")
if user_input == "0":
    user_input = input(f"Are you sure you would like to get {items[0]["name"]}.")
    if user_input == "yes":
        print(f"Great! Your total will be {items[0]["price"]} dollars.")
        total += 10.0
        user_input = input("Would you like to see the description and department?")
        if user_input == "yes":
            print(f"This item is part of the {items[0]["department"]} department, the description is shown as the following: {items[0]["description"]}")
if user_input == "1":
    user_input = input(f"Are you sure you would like to get {items[1]["name"]}.")
    if user_input == "yes":
        print(f"Great! Your total will be {items[1]["price"]} dollars.")
        total += 999.0
        user_input = input("Would you like to see the description and department?")
        if user_input == "yes":
            print(f"This item is part of the {items[1]["department"]} department, the description is shown as the following: {items[1]["description"]}")
if user_input == "2":
    user_input = input(f"Are you sure you would like to get {items[2]["name"]}.")
    if user_input == "yes":
        print(f"Great! Your total will be {items[2]["price"]} dollars.")
        total += 1999.0
        user_input = input("Would you like to see the description and department?")
        if user_input == "yes":
            print(f"This item is part of the {items[2]["department"]} department, the description is shown as the following: {items[2]["description"]}")
if user_input == "3":
    user_input = input(f"Are you sure you would like to get {items[3]["name"]}.")
    if user_input == "yes":
        print(f"Great! Your total will be {items[3]["price"]} dollars.")
        total += 1250.0
        user_input = input("Would you like to see the description and department?")
        if user_input == "yes":
            print(f"This item is part of the {items[3]["department"]} department, the description is shown as the following: {items[3]["description"]}")
user_input = input(f"Your cart is at the max limit of three, your total is ${total}, would you like to play with cash or card?")
if user_input == "cash":
    print("Great! Pay here.")
elif user_input == "card": 
    print("Alright! Scan here.")