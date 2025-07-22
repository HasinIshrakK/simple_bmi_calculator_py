height = float(input("Enter your height in cm: "))
h = height / 100  # convert to meters

weight = float(input("Enter your weight in kg: "))

bmi = round(weight / h ** 2, 2)

print("\nYour BMI is:", bmi)

if bmi < 18.5:
    v = "Underweight"
elif 18.5 <= bmi < 25:
    v = "Healthy weight"
elif 25 <= bmi < 30:
    v = "Overweight"
elif 30 <= bmi < 40:
    v = "Obese"
else:
    v = "In Danger!"

print("Category:", v)