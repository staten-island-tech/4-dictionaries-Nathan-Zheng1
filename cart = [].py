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
print("Would you like to get anything:")
for index, item in enumerate(items):
    print(index, ":" , item["name"])
user_input = input("Would you like to get any of these devices? Enter its number in the x variable section")
x = 0
user_input = input(f"Are you sure you would like to get {items[x]["name"]}.")
if user_input == "yes":
    print(f"Great! Your total will be {items[x]["price"]} dollars.")
    total += items[x]["price"]
    user_input = input("Would you like to see the description and department?")
    if user_input == "yes":
        print(f"This item is part of the {items[x]["department"]} department, the description is shown as the following: {items[x]["description"]}")
user_input = input("Would you like to continue shopping?")
if user_input == "no":
    user_input == input(f"Alright! Your total is ${total} Will you be paying with cash or card?")
    if user_input == "cash":
        print("Okay, pay up here.")
        total = 0
    elif user_input == "card":
        print("Okay, scan over here.")
        total = 0