#Palindrome or not

string = input("enter the string = ")

if string == string[::-1]:
    print("palindrome")
else:
    print("not a palindrome")
