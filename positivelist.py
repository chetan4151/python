# Write a Python program to print all positive numbers in a range.
list1=[]
n=int(input("Enter number of elements you want in list :"))
print(f"Enter {n} elements:")
for i in range(0,n):
    a=int(input())
    list1.append(a)
print("list1=",list1)
list2=[]
for i in range(0,n):
    if list1[i]>0:
        list2.append(list1[i])
print(list2)
