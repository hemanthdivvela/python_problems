#prime numbers printing

number = int(input("enter thge range of numbers = "))

if number <2:
    print("Prime numbers have 2 factors one and itself so it is not a prime numbers",number)
else:
    print("prime numbers are : ")
    for i in range(2,number+1):
        count = 0
        for j in range(2,i+1):
            if i%j==0:
                count += 1
        if count == 1:
            print(i)
