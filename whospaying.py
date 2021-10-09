import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
people = len(names)
randomperson = random.randint(0, people - 1)
paying = names[randomperson]
print(f"{paying} Will pay the bill")
