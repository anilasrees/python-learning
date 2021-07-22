#a= input("enter the first mnumber: ")
#b= input("please enter second digit : ")
#c = a+b
#print(c)
#print(list)
#list.append("orange")
#print(list)
#list.remove("apple")
#print(list)
#var = len(list)
#print(var)
#list = ["one","two","three","four","five","six","seven"]
#for num in list:
#    print(num)
#num1 = input("enter a number: ")
#b = int(num1)
#if b > 0:
#    print("it is a positive number")
#elif b < 0:
#    print("it is a negative number")
#else:
#    print("it is a zero")
"""a = int(input("input a valu : "))
b = int(input("enter a valu : "))
print("sum = " + str(a+b)
num = int(input("enter a num :"))
print("hexadecimal of "+ str(num) + " : " + str(hex(num)))
def message(name,class):
    print("hellow world"+name+class)
message("anil",3)    
message("malu"5)
def find_sum(num1,num2):
    print(num1+num2)
find_sum(10,20)
find_sum(12,34)
def find_mul():
    return 13*24
print(find_mul())
def find_square(num):
    return num*num
print(find_square(12))"""
def recursion(n):
    if n<=1:
        return n
    else:
        return n + recursion(n-1)
s = recursion(6)
print(s)        