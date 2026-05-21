
name = input("What is your name?")
print("Hello " + f"{name.title()}" + " nice to meet you!")
distance = input("Give me a number and I will convert this from Km to miles ")
miles = float(distance) / 1.609

print(distance + "Km is equal to " + f"{miles:.1f}" + " miles")