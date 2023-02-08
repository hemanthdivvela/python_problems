#Armstrong number

def arm(number):
    k = 0
    for i in number:
        k = k +pow(int(i),len(number))

    if k == int(number):
        print(number, "is Armstrong number")
    else:
        print(number,"Not an armstrong number")

number = input("enter the number = ")
arm(number)
        
