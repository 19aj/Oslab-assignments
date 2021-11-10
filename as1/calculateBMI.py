h=float(input("Heigh : "))
w=float(input("Weight : "))

bmi=w/h**2

if bmi <= 18.5:
        print("Underweight")
elif bmi > 18.5 and bmi < 25:
    print("Normal")
elif bmi > 25 and bmi < 30:
    print("Overweight")
elif bmi > 30 and bmi < 35:
    print("Obese")
else :
    print("Extremely-Obese")