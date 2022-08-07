# Write a Python program to count the number of strings where `` xss
# the string length is 2     or more and the first and last characters are the same from a 
# given list of strings.
#  ist=['abc', 'xyz', 'aba', '1221']
# result= 2.
# 
def func(a):
    i=0
    c=0
    b=[]
    while i<len(a):
        d=(a[i][::-1])
        if a[i]==d:
            b.append(d)
            c=c+1
        i=i+1
    print(b,c) 
func(['abc', 'xyz', 'aba', '1221'])
 
 
def func(a):
    i=0
    b=[]
    c=0
    while i<len(a):
        d=(a[i])[::-1]
        if a[i]==d:
            b.append(d) 
            c=c+1        
        i=i+1
    print(c)
func(['abc', 'xyz', 'aba', '1221'])

