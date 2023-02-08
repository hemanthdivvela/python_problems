# Given number check prime number or not a prime number

number = int(input("Enter a number = "))
count = 0

if number <2:
    print("the number of positive divisors or factors is only one",number)
    
else:
    for i in range(2,number+1):
        if number % i == 0:
            count += 1
    if count == 1:
        print("it is prime number",number)
    else:
        print("it is not a prime number",number)
