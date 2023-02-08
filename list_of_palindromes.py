#Palindrome in the given list

string = list(input("enter the  more string = ").split())

for i in range(len(string)):
    if string[i] == string[i][::-1]:
        print(string[i],"palindrome")
    else:
        print(string[i],"not a palindrome")
