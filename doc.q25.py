# Q25. Given a list of numbers, write a Python program to count positive 
# and negative numbers in a List using function.
# list1 = [2, -7, 5, -64, -14]
# Output: pos = 2, neg = 3


def vidya(a):
    i=0
    b=0
    c=0
    while i<len(a):
        if a[i]>0:
           b=b+1
        else:
            c=c+1
        i=i+1    
    print(b,c)
vidya([2, -7, 5, -64, -14])
