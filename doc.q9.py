
# Q9.Write a Python program to generate and print a list of first and last 5 elements where 
#   the values are square of numbers between 1 and 30 (both included).
# Output :-([Write a Python program to generate and print a list of first and last 5 elements where 
#   the values are square of numbers between 1 and 30 (both included).
# Output :-([1, 4, 9, 16, 25], [676, 729, 784, 841, 900]).



def list(a,c):
    i=0
    m=[]
    b=[]
    while i<len(a):
            b.append(a[i]*a[i])
            m.append(c[i]*c[i])
            i=i+1
    print(b,m)
list([1,2,3,4,5],[26,27,28,29,30])

