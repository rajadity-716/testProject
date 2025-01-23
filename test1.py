height=float(input("Enter your height in meter\n"))
weight=float(input("Enter your weight in kg\n"))
#weight_int=float(height)
bmi=weight/(height**2)
#bmi=weight_int/(height_int**2)
if bmi<=18.5:
    print("Underwight")
elif bmi>18.5 and bmi<=25:
    print("normal weight")
elif bmi>25 and bmi<=30:
    print("slightly overweight")
elif bmi>30 and bmi<=35:
    print("obese")
else:
    print("clinally obese")
