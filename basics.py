"""
#input values and find sum

valu1 = int(input("enter the first dgit: "))
valu2 = int(input("enter the second value : "))
sum = valu1 + valu2
print("sum of these two numbers is : "+str(sum))


#if_elif_else

i = int(input("enter an integer :"))
if i ==0:
    print("it is a zero")
elif i >=1:
    print("it is a positive number")
elif i <=-1:
    print("it is a negative number")
    """

#palindrome 

string = input("enter a word : ")
rev_string = string [::-1]
if string == rev_string :
    print("this word is a palindrome.")
else:
    print("this is not a palindrome.")
