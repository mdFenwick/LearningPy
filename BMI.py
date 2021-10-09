height = input("enter your height in m:")
weight = input("enter your weight in kg:")

bmi = float(weight) / float(height)**2
bmi_int = int(bmi)

if bmi_int < 18.5:
    print(f"Your BMI is {bmi_int}. You are underweight")
elif bmi_int < 25:
    print(f"Your BMI is {bmi_int}. You have a normal weight")
elif bmi_int < 30:
    print(f"Your BMI is {bmi_int}. You are slightly overweight")
elif bmi_int < 35:
    print(f"Your BMI is {bmi_int}. You are obese")
else:
    print(f"Your BMI is {bmi_int}. You are clinically obese")
