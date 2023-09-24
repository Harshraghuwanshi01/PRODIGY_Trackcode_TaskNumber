import random
n=random.randint(1,100)
g=1
a=int(input("enter the no"))
g_over=False
while not g_over:
    if a==n:
        print(f"you win and you found the no in {g} times")
        g_over=True
    else:
        if a<n:
            print("too low")
            g+=1
            a=int(input("again give your no"))
        else:
            print("too high")
            g+=1
            a=int(input("again give yr no"))
