# duplicates in string

def string(word):
    res = []
    for i in word:
        k = word.count(i)
        if k>1 and i not in res:
            res.append(i)
            print(i)
           
word = input("enter the string = ")
string(word)
