def calculate_bmi(weight, height):
    return weight / (height ** 2)

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))
bmi = calculate_bmi(weight, height)
print(f"Your BMI is: {bmi:.2f}")
