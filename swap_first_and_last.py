#swap first number and last number

def lst(l):
    print("original list = ",l)
    temp = l[0]
    l[0] = l[-1]
    l[-1] = temp
    print("after swapping list",l)

    l[0],l[-1] = l[-1],l[0]
    print("again swapping list",l)

l = list(map(int,input("Enter the list of number = ").split()))
lst(l)
