#Find Second Largest Number in a List
def lst(l1):
    l1.sort()
    k = l1[-2]
    print(k)
    return k


l1 = [1,2,3,4]
lst(l1)


