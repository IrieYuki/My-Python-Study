from random import randint

x = randint(1, 100)

y = randint(1, 100)
print("猜测数字为",y)

m = 0
n = 101
time = 0

while y != x:
    time += 1
    if y > x:
        n = y
        print("猜大了")
        
    elif y < x:
        m = y
        print("猜小了")

    print("范围为",m+1,"，",n-1)
    y = randint(m+1, n-1)
    print("猜测数字为",y)

else:
    time += 1
    print("答对了!目标数字为",y)
    print("总共猜测了",time,"次")