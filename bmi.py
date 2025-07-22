import math

height = int(input("Enter your height in cm: "))

h = height / 100

weight = int(input("Enter your weight in kg: "))

bmi = math.ceil((weight / h ** 2)*100) / 100


print("Your BMI is: ", bmi)

if bmi < 18.5:
    v = "Under weight"
elif bmi >= 18.5 and bmi < 25:
    v = "Healthy weight"
elif bmi >= 25 and bmi < 30:
    v = "Overweight"
elif bmi >= 30 and bmi < 40:
    v = "a Fat!"
else:
    v = "in Danger!!!"

print("You are", v)