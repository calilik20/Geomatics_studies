num = int(input("Enter a number :"))

factorial = 1

""""
check if the number is negetive, positive or zero 
"""

if num < 0 :
  print("Sorry, factorial does not exist for negetive numbers")
elif num == 0 :
  print("the factorial of 0 is 1")

else: 
  for i in range (1, num+1):
    factorial= factorial*i

print("the factorial of", num, "is",factorial)

