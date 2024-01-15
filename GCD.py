#finding the GCD of two input number

# lets define a function
def computeGCD (x,y):
  #choose the smaller number 
  if x>y:
    smaller =y
  else:
    smaller =x
  for i in range (1, smaller+1):
      if ((x%i == 0) and (y%i ==0)):
          gcd = i
  return gcd

num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number: "))
print ("GCD of",num1,"and",num2,"is",computeGCD(num1,num2))
