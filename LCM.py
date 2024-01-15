#finding the LCM of two input number

# lets define a function

def lcm(x,y):
    """ this function takes two integers and return the LCM """
    #choose the greater number
    if x>y:
      greater=x
    else:
      greater=y
    while(True):
       if ((greater%x==0) and (greater %y==0)):
           lcm = greater
       break
    greater +=1
  
    return lcm
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
print("LCM of", num1,"and",num2,"is",lcm (num1,num2))
