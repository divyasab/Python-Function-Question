# .Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Output : 20.
def list(a):
    i=0
    s=0
    b=[]
    while i<len(a):
        s=s+a[i]
        i=i+1
    print(s)
list([8, 2, 3, 0, 7])