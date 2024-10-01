
POUND_CONV = 0.453592
INCH_CONV = .0254

def bmi_func(height, weight):
 kg = weight * POUND_CONV 
 m = height * INCH_CONV
 BMI = int(kg / (m * m))
 return BMI


height = int(input("What is your height in inches: "))
weight = int(input("What is your weight in pounds: "))

bmi_result = bmi_func((height), (weight))

if bmi_result < 18.5:
    print(bmi_result)
    print("Your underweight")
if bmi_result == 18.5 <= bmi_result < 24.9:
    print(bmi_result)
    print("Your a normal weight")
if bmi_result == 25 <= bmi_result < 29.9:
    print(bmi_result)
    print("Your overweight")
if bmi_result == bmi_result >= 30:
    print(bmi_result)
    print("Your obese")