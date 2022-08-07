# Q7.Write function bmi that calculates body mass index (bmi = weight / height2).

# if bmi <= 18.5 return "Underweight"

# if bmi <= 25.0 return "Normal"

# if bmi <= 30.0 return "Overweight"

# if bmi > 30 return "Over"

def list():
    a=int(input("enter the number"))
    if  a<=18.5:
        print("Underweight")
    if a<=25.0:
        print("Normal")
    if a<=30.0:
        print("Overweight")
    else:
        print("obses")
list()
