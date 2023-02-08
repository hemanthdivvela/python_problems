#Swapping

a= int(input())
b = int(input())
print("before swap a,b values",a,b)
a,b = b,a
print("After swap a,b Values",a,b)
a,b = a+b-a,b+a-b
print(a,b)
