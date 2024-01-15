top = int(input("enter the numerator:"))
bottom = int(input("enter the denominator:"))
if top % bottom==0 and bottom!=0:
    print("The numerator is evenly divided by the denominator.")
else:
    print("The fraction is not a whole number.")
