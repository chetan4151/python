# Write a Python program to accept a filename from the user and print the extension of that
filename=input("Input the Filename:")
for i in range (0,len(filename)):
    if (filename[i]=='.'):
        break
if (filename[i+1:1000]=="py"):
    print("The extension of the file is : python")
elif (filename[i+1:1000]=="java"):
    print("The extension of the file is : Java")
elif (filename[i+1:1000]=="cpp"):
    print("The extension of the file is : C++")
elif(filename[i+1:1000]=="html"):
    print("The extension of the file is : html")
elif (filename[i+1:1000]=="js"):
    print("The extension of the file is : javascript")
elif (filename[i+1:1000]=="cpp"):
    print("The extension of the file is : C++")
elif (filename[i+1:1000]=="c"):
    print("The extension of the file is : C")
elif (filename[i+1:1000]=="css"):
    print("The extension of the file is : CSS")
elif (filename[i+1:1000]=="r"):
    print("The extension of the file is : R")
