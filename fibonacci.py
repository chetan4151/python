# Write a Python Program for Fibonacci numbers.
n=int(input())
i=0
j=1
if n<=0:
   print("Please enter a positive integer")
else:
    for val in range(0,n):
        print(i)
        k=i+j
        i=j
        j=k
