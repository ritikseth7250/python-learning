# menu={"pizza":3.00,
#       "sauce":4.50,
#       "popcorn":6.00,
#       "fries":2.50,
#       "chips":1.00,
#       "pretzel":3.50,
#       "soda":3.00,
#       "lamonade": 4.24,
#       }
# cart =[]
# total =0

# for key, value in menu.items():
#     print(f"{key:10}: ${value:.2f}")
# print("------------------------")

# while True:
#     food=input("Select the item (q to quit)").lower()
#     if food == "q":
#         break
#     elif menu.get(food) is not None:
#         cart.append(food)

# print(cart)

# for food in cart:
#     total=total+menu.get(food)
#     print(food, end= " ")
# print()
# print(f"Total is: ${total:.2f}")

# person={
#     "Name":"Ritik",
#     "Age" : 23,
#     "course": "B.tech"
#     }

# person["city"]= "Durgapur"
# person.pop("Age")

# print(person)

students ={
}
students["Ritik"] =85
students["Rahul"] =78
students["Aman"] =92
name=input("Enter the name: ")


print(name,"'s marks=",students[name])
