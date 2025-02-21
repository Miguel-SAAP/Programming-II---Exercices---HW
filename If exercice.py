def calculate_net_salary():
    try:
        gross = float(input("Gross salary? "))
        children = int(input("what is you number children ? "))
        if gross < 1000: tax = 0.10
        elif gross < 2000: tax = 0.12
        elif gross < 4000: tax = 0.14
        else: tax = 0.18
        if gross < 2000: tax = tax - (0.01 * children)
        else: tax = tax - (0.005 * children)
        if tax < 0: tax = 0  # tax can't be negative
        net = gross * (1 - tax)
        print("Your net salary is:", net)

    except:
        print("Invalid input, try again")
        calculate_net_salary()

calculate_net_salary()
