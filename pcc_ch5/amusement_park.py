age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

# more concise version
if age < 4:
    price = 0
elif age < 18:
    price = 25
# additional elif statements can be added
elif age < 65:
    price = 40
# else can be omitted and replaced with a conditional elif
elif age >= 65:
    price = 20
else:
    price = 20

print(f"Your admission cost is ${price}.")
