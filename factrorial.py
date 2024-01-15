def factorial():
    number = int (input("Enter an integer number: "))
    factorial = 1
    for i in range(1, number+1):
        factorial *= i
    print ("Factorial of", number, "is", factorial)
factorial ()
