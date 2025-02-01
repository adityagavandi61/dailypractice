## using recursion 

def fab_recur(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fab_recur(n-1) + fab_recur(n-2)

for i in range(10):
    print(fab_recur(i),end=" ")

# using iteration

def fab_iter(n):
    a,b = 0,1
    for i in range(n):
        print(a,end=" ")
        a,b = b,a+b

fab_iter(10)

