import math
print("\t  CALCULATOR   ")
def sum(a,b):
    a+=b
    
    print ("The sum of these numbers is : "+str(a))

def sub(a,b):
    if a>b:
        a-=b
        
        print("\nThe difference is : "+str(a))
    else:
        b-=a
        
        print("\nThe difference is : "+str(b))
def mul(a,b):
    a*=b
    
    print("\nThe product is : "+str(a))
def div(a,b):
    q=a/b
    r=a%b
    print(" the quotient is : "+str(q))
    print("  the remainder is :"+str(r))
def sqrt(a):
    x=math.sqrt(a)
    
    print("\nthe squre root is : "+str(x))

def sqr(a):
    t=a*a
    print("The square is : "+str(t))


while(True):
    print("\tchoose the operation you want to perform : ")
    print("\t1.ADDITION")
    print("\t2.SUBTRACTION")
    print("\t3.MULTIPLICATION")
    print("\t4.DIVISION")
    print("\t5.SQUARE ROOT")
    print("\t6.SQUARE")
    print("\t7.EXIT")
    
    choice = int(input('>'))
    
    if choice==1:
        print("Enter two numbers : ")
        num1 = int(input('>'))
        num2 = int(input('>'))
        sum(num1,num2)
        
    elif choice==2:
        print("\n\nEnter two numbers : ")
        num1=int(input('>'))
        num2=int(input('>'))
        sub(num1,num2)
       
    elif choice==3:
        num1=int(input("Enter the first number"))
        num2=int(input("Enter the second number"))
        mul(num1,num2)
       
    elif choice==4:
        num1=int(input("Enter the first digits"))
        num2=int(input("Enter the second number"))
        div(num1,num2)
    elif choice==5:
        num1=int(input("Enter the number"))
        sqrt(num1)
     
    elif choice==6:
        num1=int(input("Enter the value : "))
        sqr(num1)
    else:
        print("you choose to exit...thank you...")
        break
