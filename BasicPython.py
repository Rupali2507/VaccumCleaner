# Print in python

print("Hello!", end= " ")
print("World")


#Sum
a=20
b=30
c=a+b
print("sum of two numbers 20 and 30 is ",c)

print("xyz", end=" read ")
print("abc")

print("xyz\nabc")
print("xyz\tabc")


var1 = "Hello World!"
var2 = 10
var3 = 13.5
print(var1, var2, var3)
print(type(var1))
print(type(var2))
print(type(var3))
print(var2+var3)


var4 = "36"
print(int(var4))

# Taking input
print("Enter a number: ")
var5 = input()
print("Entered number is: ", var5)



# #Calculator

#Taking input of two numbers
print("Enter first number: ")
var1 = int(input())
print("Enter second number: ")
var2 = int(input())

#performing and printing the result of basic arithmetic operations
print("Sum of given numbers is: ", var1+var2)
print("Difference of given numbers is: ", var1-var2)
print("Product of given numbers is: ", var1*var2)
print("Quotient of given numbers is: ", var1/var2)



#List
stList = ["apple", "banana", "orange", "cherry", "mango"]
print(stList)
numberList = [2, 6, 7, 8, 10]
print(numberList)
fpList = [10.1, 34.9, 34.7]
print(fpList)
booleanList = [True, False, True]
print(booleanList)
complexList = ["apple", 2, 10.1, True]
print(complexList)


#Properties of List
print(stList[2])
print(len(stList))
print(type(stList))


thisList = list(("Apple", "Mango", "Banana"))
print(thisList)



stList.sort()
print(stList)

stList.reverse()
print(stList)

stList.append('berry')
print(stList)

stList.append(numberList)
print(stList)

stList.insert(2,"papaya")

stList.pop()
stList.index("apple")
stList.count(thisList)
stList.copy()

print(stList)



#Conditional Statements in Python
num = int(input("Enter a number: "))
if num>0:
  print("Positive number")
elif num<0:
  print("Negative number")
else:
  print("Zero")


# Function

def myFunc(fname):
  print(fname+ "ABC")
myFunc('Krish')


def sum(var1, var2):
  print(var1+var2)

var1 = int(input("Enter first number: "))
var2 = int(input("Enter second number: "))
sum(var1, var2)


#Loops
i=1
while i<6:
  print(i,end=" ")
  i=i+1

print("\n")

i=1
while (i<6):
  if i==3:
    break
  print(i,end=" ")
  i=i+1  


print("\n")

for i in range(1,10):
  print(i,end=" ")
print("\n")
for i in range(10):
  print(i,end=" ")  


print("\n")

fruits = ["Apple", "Banana", "Orange"]
for i in fruits:
  print(i)  