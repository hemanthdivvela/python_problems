#factorial of given number

number = int(input("enter a number :"))
k = 1
for i in range(1,number+1):
    k = k*i

print("factorial of give number is = ",k)
