print("welcome user to calculator")
def sum(num1,num2):
    sum=num1+num2
    return sum

def subtract(num1,num2):
    subtract=num1-num2
    return subtract

def division(num1,num2):
     division=num1/num2
     return division

def multiply(num1,num2):
      multiply=num1*num2
      return multiply


while True:
  num1=float(input("enter 1st number"))
  num2=float(input("enter 2nd number"))
  operation=input("enter operation to be performed")
  if(operation=="+"):
    print("addition performed",sum(num1,num2))
  elif(operation=="-"):
    print("subtraction performed",subtract(num1,num2))
  elif(operation=="*"):
    print("multiplcation performed",multiply(num1,num2))
  elif(operation=="/"):
     if (num2==0):
      print("invalid operation division not performed")
  else:
    print("division performed",division(num1,num2))   
  choice =input("want to perform another operation?(yes/no)")
  if(choice=="no"):
      print("terminate")
      break  

