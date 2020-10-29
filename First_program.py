
breakfast = ["egg", "bacon", "salmon"]
drink = ["milk", "juice", "coke"]
lunch = ["burger", "pizza"]
print("Hi ! Good Morning. Please have a seat. What would you like to have?")
order = input("Breakfast, Drink or Lunch: ")
b="breakfast"
d="drink"
l="lunch"
if order == b:
    print("Here is your breakfast option",(breakfast))
elif order == d:
    print("Here is your drink option",(drink))
elif order == l:
    print("Here is your lunch option",(lunch))
else:
    print("order again")

