age = input("What is your current age?")
age_int = int(age)

years_remaining = 90 - age_int
days = years_remaining * 365
weeks = years_remaining * 52
months = years_remaining * 12

message = f"You have {days} Days, {weeks} Weeks, and {months} Months"
print(message)
