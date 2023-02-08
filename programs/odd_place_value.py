#Remove Odd Indexed Characters in a string

def sli(word):
    for i in range(0,len(word),2):
        print(word[i],end="")

word = input("enter a long string = ")
sli(word)

