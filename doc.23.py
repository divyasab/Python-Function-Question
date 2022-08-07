def test(x = 1, y = 2):
    x = x + y
    y += 1
    print(x, y)
test()

def func(x=1,y=2):
    x=x+y
    y=y+1
    print(x,y)
func()