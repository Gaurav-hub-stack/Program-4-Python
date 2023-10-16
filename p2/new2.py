#conditional
# if Condition
# Example condition
x = 5
if x > 0:
    print("x is positive")
else:
    print("x is not positive")
# first Program
marks  = float(input("Enter Your Mark:"))
if (marks>=30):
    print("pass")
    print("haapy")
if (marks<30):
   print("fail")
   print("sad") 
print("thaks You")

if "":
	  print("mango")
if "hi":
	  print("apple")
else:
	  print("orango")
	#WAP to check even and odd
num = int(input("Enter your Number:"))
if num%2==0:
	 print("Even")
else:
	print("odd")
#wap to user and password Program
user = input("enter name:")
pwd=input("enter password:")
if user =="admin" and pwd =="bharat":
	print("Valid user")
else:
	print("invalid user")
# WAP To Marks for Div
Marks = float(input("Enter Marks:"))
if marks<30:
	print("fail")
if marks>=45:
	 print("3rd div")
if marks>=60:
	 print("1st div")

x = 10
if x > 10:
		print("x is greater than 10")
elif x == 10:
		print("x is equal to 10")
else:
		print("x is less than 10")

# Salary Calu Program 
sal = float(input("enter sal:"))
if sal>=0 and sal<=10000:
	print("low salary")
elif sal>10000 and sal<35000:
	print("avg sal")
elif sal>=35000:
	print("high sal")
else:
	print("invalid sal")
print("thank you")


#WAP to Salary Pay
amt = float(inpiut("enter amout:"))
if amt>=1000:
	amt=amt-50
	print("50 cashback added")
print("final amout: ",amt)