# Q17. Write a function to tell user if he/she is able to vote or not.
# ( Consider minimum age of voting to be 18. )
def func():
    age=int(input("enter the number"))
    if age>=18:
        print("able to vote")
    else:
        print("not able to vote")
func()
