# Name: Mudassir Munir
# PSEB ID: PSEB-2026-010784
# Date: 06-11-2026

# 1.Warm-up Exercise:
# Create a program that takes user input for their name, age, class, and city. Then, display this information in a formatted manner.

name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))
student_class = input("Enter Your Class: ")
city = input("Enter Your City: ")

print("===============STUDENT CARD=================")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Class: {student_class}")
print(f"City: {city}")
print("============================================")

print(type(name))
print(type(age))
print(type(student_class))
print(type(city))

# 2.Build -Shop Bill:
#create a program that takes user input for an item name, price, and quantity. Then, calculate the subtotal, apply a discount of 5%, add a tax of 17%, and display the final bill in a formatted manner.

print("===============SHOP BILL====================")
item = input("Enter the item name: ")
price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity: "))

subtotal = price * quantity

discount = subtotal * 0.05

discounted_amount = subtotal - discount
tax = discounted_amount * 0.17
final_bill = discounted_amount + tax

print("===============================")
print(f"Item: {item}")
print(f"Price: Rs{price:.2f}")
print(f"Quantity: {quantity}")
print(f"Subtotal: Rs{subtotal:.2f}")
print(f"Discount: Rs{discount:.2f}")
print(f"Discounted Amount: Rs{discounted_amount:.2f}")
print(f"Tax: Rs{tax:.2f}")
print(f"Final Bill: Rs{final_bill:.2f}")
print("===============================")

#3.Challenge - Unit Converter:
# Create a program that takes user input for temperature in Celsius and distance in Kilometers. Then, convert the temperature to Fahrenheit and Kelvin, and the distance to Miles and Meters. Display the results in a formatted manner.

print("===============UNIT CONVERTER================")
celcius = float(input("Enter temperature in Celsius: "))
kilometers = float(input("Enter distance in Kilometers: "))

# convert temperature
fahrenheit = (celcius * 9/5) + 32
kelvin = celcius + 273.15
# convert distance
miles = kilometers * 0.621371
meters = kilometers * 1000

print("==============Unit Converter=================")
print(f"Temperature in Celsius: {celcius}°C")
print(f"Temperature in Fahrenheit: {fahrenheit}°F")
print(f"Temperature in Kelvin: {kelvin}K")
print("---------------------------------------------")
print(f"Distance in Kilometers: {kilometers} km")
print(f"Distance in Miles: {miles} miles")
print(f"Distance in Meters: {meters} m")
print("=============================================")