
def add(a,b):
    return a+b
    
def subtract(a,b):
    return a-b
    
def multiply(a,b):
    return a*b

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("you cannot divide by zero")
print("Calculator")
print("chose an operation")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
n1=int(input("Enter a Choice (1/2/3/4)"))
if(n1<1 and n1>4):
    print (n1)
    print("invalid choice")
else:
    try:
        num1=float(input("enter a number "))
        num2=float(input("enter a number "))
        if n1==1:
            print("result",add(num1,num2))
        elif n1==2:
            print("result",subtract(num1,num2))
        elif n1==3:
            print("result",multiply(num1,num2))
        elif n1==4:
            print("result",divide(num1,num2))
        else:
            print("invalid choice")
    except ValueError:
        print("please input a number")
    

