def multiple_of_6():
    while True:
        try:
            n = int(input("Enter a multiple of 6: "))
            if n % 6 == 0:
                return n
            else:
                print("That is not a multiple of 6")
        except:
            print("Invalid input")

print(multiple_of_6())
