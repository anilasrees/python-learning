import math
print("\t  CALCULATOR   ")
def sum(a,b):
    a+=b
    return a

def sub(a,b):
    if a>b:
        a-=b
        return a
    else:
        b-=a
        return b
def mul(a,b):
    a*=b
    return a
def div(a,b):
    q=a/b
    r=a%b
    print(" the quotient is : "+str(q))
    print("  the remainder is :"+str(r))
def sqr(a):
    x=math.sqrt(a)
    return x


while(True):
    print(" choose the operation you want to perform : ")
    print("\t1.ADDITION")
    print("\t2.SUBTRACTION")
    print("\t3.MULTIPLICATION")
    print("\t4.DIVISION")
    print("\t5.SQUARE ROOT")
    print("\t6.EXIT")
    
    choice = int(input('>'))
    
    if choice==1:
        print("Enter two numbers : ")
        num1 = int(input('>'))
        num2 = int(input('>'))
        s=sum(num1,num2)
        print ("The sum of these numbers is : "+str(s))
    elif choice==2:
        print("\n\nEnter two numbers : ")
        num1=int(input('>'))
        num2=int(input('>'))
        b = sub(num1,num2)
        print("\nThe difference is : "+str(b))
    elif choice==3:
        num1=int(input("Enter the first number"))
        num2=int(input("Enter the second number"))
        p=mul(num1,num2)
        print("\nThe product is : "+str(p))
    elif choice==4:
        num1=int(input("Enter the first digits"))
        num2=int(input("Enter the second number"))
        div(num1,num2)
    elif choice==5:
        num1=int(input("Enter the number"))
        r=sqrt(num1)
        print("\nthe squre root is : "+str(r))
    else:
        print("you choose to exit...")
        break
