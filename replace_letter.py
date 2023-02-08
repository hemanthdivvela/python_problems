#Replace All Occurrences of ‘a’ with $ in a String

def rpl(word,i,j):
    print(word)
    k = word.replace(i,j)
    print(k)

word = input("enter the string = ")
i = input("enter which letter you change = ")
j = input("enter replacing letter = ")

rpl(word,i,j)
