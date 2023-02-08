#search the word in last

array = list(input("enter a list of words ").split())
a = input("enter the search  word")
for i in range(0,len(array)):
    if array[i].startswith(a):
        print(array[i])
