#fibnoacci numbers

def fib(a):
    if a<=1:
        return a
    else:
        return fib(a-1)+fib(a-2)

a=int(input("enter any number"))
print(fib(a))