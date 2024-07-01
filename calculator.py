# Python program to make a simple calculator using function

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

no1=eval(input("Enter the first number: "))
no2=eval(input("Enter the second number: "))

print("Select the operation you want to perform")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

while(True):
    choice=int(input("Enter the choice from (1/2/3/4/5): "))
    if choice in (1,2,3,4,5):
      if choice==1:
        print("Addition of two numbers", no1,"+",no2,"=", add(no1,no2))  
        break
      elif choice==2:
        print("Subtraction of two numbers", no1,"-",no2,"=", subtract(no1,no2))
        break
      elif choice==3:
         print("Multiplication of two numbers", no1,"*", no2, "=", multiply(no1,no2))
         break
      elif choice==4:
         print("Division of two numbers", no1,"/", no2, "=", divide(no1,no2)) 
         break 
      elif choice==5:
         print("Exiting the calculator")
         break
         exit()
         

else:
    print("Invalid choice try again")

        