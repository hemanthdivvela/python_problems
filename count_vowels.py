# how many vowels in string


def string(word):
    vowels = "AEIOUaeiou"
    count = 0
    for i in word:
        if i in vowels:
            count += 1
    print("total vowels in given word = ",count)

word = input("enter a string = ")
string(word)
