# string slicing

def string(word):
    for i in range(2,len(word)):
        print(word[i],end="")
    print()
    print(word[2:])

word = input("enter a word = ")
string(word)
