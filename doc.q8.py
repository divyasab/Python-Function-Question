# Q8.Write a Python function that accepts a string and calculate the number of upper
#  case letters and lower case letters. Go to the editor
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Uppercase characters : 3
# No. of Lower case Characters : 12
def list(a):
    i=0
    b=0
    c=0
    while i<len(a):
        if a[i]>="A"and a[i]<="Z":
            b=b+1
        elif a[i]>="a" and a[i]<="z":
           c=c+1
        i=i+1
    print(b)
    print(c)
list("The quick Brow Fox")
