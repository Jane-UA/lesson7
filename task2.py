a = int(input())
b = int(input())

def square(a, b):
   return a**2/b
x = square(a, b)
print(x)
try:
    if b == 0:
        raise ZeroDivisionError("!")
except ZeroDivisionError as v:
    print(v)

