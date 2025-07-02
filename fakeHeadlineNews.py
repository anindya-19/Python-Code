import random as rn

subjects = [
    "Virat Kohli",
    "Rohit Sharma",
    "Salman Khan",
    "Shahrukh Khan",
    "Taxi wala",
    "Auto wale bhaiya"
]

actions = [
    "launches",
    "dances",
    "eats",
    "declares war on",
    "order",
    "celebrates"
]

places_or_things = [
    "at Red Fort",
    "Mumbai Local Train",
    "Plate of Samosa",
    "Inside Parliamen",
    "at Ganga Ghat",
    "during IPL match"
]

while True:
    subjectChoice = rn.choice(subjects)
    actionChoice = rn.choice(actions)
    placesChoice = rn.choice(places_or_things)

    headLine = f"BREAKING NEWS: {subjectChoice} {actionChoice} {placesChoice}"

    print("\n",headLine)

    user_input = input("Do you want another headline? (yes/no): ").strip().lower()

    if user_input == 'no':
        print("Thank for using headline generator!!")
        break
    

