# Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Output : "dcba4321".
def list(a):
    i=1
    sum=""
    while i<len(a):
        sum=sum+(a[-i])
        i=i+1
    print(sum)
list("1234abcd")
