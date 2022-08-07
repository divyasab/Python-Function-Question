
# Q12.Numbers ending with zeros are boring.

# They might be fun in your world, but not here.

# Get rid of them. Only the ending ones.

# 1450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105



def func(a):
    i=0
    b=[]
    while i<len(a):
        while a[i]>0 or a[i]<0:
            if a[i]%10!=0:
                b.append(a[i])
                break
            a[i]//=10
        i=i+1
    print(b)
func([1450])
func([960000])
func([1050])
func([-1050])


