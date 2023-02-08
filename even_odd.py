#print even numbers and odd numbers separeatly

number = int(input("enter a number = "))
print("even numbers = ")
for i in range(number):
    if i % 2==0:
        print(i,end=" ")
print()

print("odd numbers = ")
for i in range(number):
    if i%2!=0:
        print(i,end=" ")
        
