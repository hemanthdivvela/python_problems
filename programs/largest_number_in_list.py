#Python Program to Find Largest Number in a List

def lst(l1):
    #k = max(l1)
    max_value =l1[0]
    for i in range(len(l1)-1):
        if max_value < l1[i+1]:
            max_value = l1[i+1]
        else:
            max_value = l1[i]
    print(max_value)

l1 = list(map(int,input("enter the numbers:").split()))
lst(l1)
