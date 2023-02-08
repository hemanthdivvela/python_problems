#Merge Two Lists and Sort it

def lst(l1, l2):
    l1.extend(l2)
    l1.sort()
    res = []
    for i in range(len(l1)):
        k = int(l1[i])
        res.append(k)
    print(res)

l1 = list(input("enter the list:").split())
l2 = list(input("enter the list:").split())
count = 0
count1 = 0
for i in range(len(l1)):
    if l1[i].isdigit():
        count += 1
for i in range(len(l2)):
    if l2[i].isdigit():
        count1 += 1
if count == len(l1):
    if count1 == len(l2):
        lst(l1,l2)
    else:
        print("your enter worng please enter only number 12")
else:
    print("you enter worng please enter only number 11")

    


