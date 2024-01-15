for row in range(1, 10):
    print(*(f"{row*col:3}" for col in range(1, 10)))
