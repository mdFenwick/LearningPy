# Make a flowchart to figure out steps
year = int((input("What year do you want to check for a Leap Year?")))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a Leap year")
        else:
            print(f"{year} is not a Leap year")
    else:
        print(f"{year} is a Leap year")
else:
    print(f"{year} is not a Leap year")
