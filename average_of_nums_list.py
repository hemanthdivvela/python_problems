#Find Average of a List
def lst(l1):
    k = sum(l1)
    l = len(l1)
    print("Average of the list of given numbers =", k/l)

l1 = list(map(int,input("enter the list of  number").split()))
lst(l1)

