# Q31. Your goal is to return multiplication table for number that is always
#  an integer from 1 to 10.For example, a multiplication table (string) for 
#  number == 5 
# looks like below:- 1 * 5 =
def func(a):
    i=1
    while i<=10:
        print(i,"*",a,"=",a*i)
        i=i+1
func(5)

