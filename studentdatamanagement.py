import csv
def display():
    print("1. Enter Student's Data")
    print("2. View Students Data")
    print("3. Quit")
def fun1():
    while True:
        abc = []
        for i in data:
            temp = input(f"Enter {i} :\n")
            if i==data[4]:
                while (len(temp)!=10 or temp.isnumeric()==False):
                    print("Phone number should be of 10 digits,please enter again!!")
                    temp = input(f"Enter {i} :\n")
            abc.append(temp)
        with open(filename, "a") as f:
            writer = csv.writer(f)
            writer.writerows([abc])
        condn = input("Do you want to enter data for another student(yes/no) :\n")
        if condn == "no":
            break
def fun2():    
    print("                                                  ||||OUR STUDENTS DATA||||\n")
    with open(filename, "r") as f:
        reader = csv.reader(f)
        print("\n-------------------->>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<------------------------")
        for row in reader:
            for x in row:
                print(x, end="\t |")
            print("\n")
print("                                     ||||Welcome to Students Data Management System||||\n")
while True:
    filename = input("please enter the name of csv file you want to create to store students data:\n")
    try:
        open(filename, "x")
        break
    except:
        print("\nfile is aready present please use another name")
data = ['Name', 'Class', 'DOB','Email','phone number', 'Address']
with open(filename, "w") as f:
    writer = csv.writer(f)
    writer.writerows([data])
while True:
    display()
    choice = input("Enter your choice: ")
    if choice == '1':
        fun1()
    elif choice == '2':
        fun2()
    else:
        break
print("||||Have a Nice Day||||")
