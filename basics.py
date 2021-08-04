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
    

#palindrome 

number = input("enter a number : ")
string = str(number)
rev_string = string [::-1]
if string == rev_string :
    print("this number is  palindrome.")
else:
    print("this number is not palindrome.")

# fibonacci series

count = int(input("how many numbers you want in fibonacci series ? please enter the number : "))
n1,n2 = 0,1
sum = 0
if count <=0:
    print("please enter a number grater than zero!!")
else:
    for i in range(count):
        print(sum)
        n1 = n2
        n2 = sum
        sum =n1+n2

    
def fabonacci(num):
    sum= n1+n2
    

num = int(input("enter number"))
n1 = 0
n2 = 1
sum = 0
fabonacci(num)
print(sum)

"""
#calculate the tax

#if income is less than 150000 then no tax
#if taxable income is 150001 - 300000 then charge 10% tax
#if taxable income is 300001 - 500000 then charge 20% tax
#if taxable income is above 500001 then charge 30% tax

min1 = 150001
max1 = 300000
rate1 = 0.10
min2 = 300001
max2 = 500000
rate2 = 0.20
min3 = 500001
rate3 = 0.30

income = int(input("enter the income : "))
taxable_income =income -150000
if (taxable_income <=0):
    print("no tax")
elif(taxable_income>=min1 and taxable_income<max1):
    tax = (taxable_income - min1) *rate1
elif(taxable_income>min2 and taxable_income<max2):
    tax = (taxable_income - min2) * rate2
else:
    tax = (taxable_income-min3) *rate3
print("TAX = ",str(tax))    