# Q19.What is the output of the following code snippet?

# def func(x = 1, y = 2):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          vd
#     x = x + y
#     y += 1
#     print(x, y)
# func(y = 2, x = 1)
#   A. 1 3
# B. 2 3
# C. The program has a runtime error because x and y are not defined.
# D. 3 2
# E. 3 3
def func(a=1,b=2):
    a=a+b
    b=b+1
    print(a,b)
func(b=2,a=1)