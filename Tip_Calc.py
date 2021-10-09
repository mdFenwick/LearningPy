print("Tip Calculator")

bill = float(input("Total Amount?"))
tip = int(input("How much tip 10, 15, 20?"))
split = int(input("How many people are you splitting with?"))

tip_percent = tip / 100
total_tip = bill * tip_percent
total_bill = bill + total_tip
split_bill = total_bill / split
final_amount = round(split_bill, 2)

print(f"Each person should pay: ${final_amount}")
