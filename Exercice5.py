try:
    gross = float(input("Enter the gross salary: "))
    children = int(input("Enter the number of children: "))

    if gross < 1000:
        tax_rate = 0.10
    elif gross < 2000:
        tax_rate = 0.12
    elif gross < 4000:
        tax_rate = 0.14
    else:
        tax_rate = 0.18

    tax_cut = 0.01 if gross < 2000 else 0.005
    tax_rate -= children * tax_cut

    net_salary = gross * (1 - max(0, tax_rate))  # Empêcher un taux d'imposition négatif
    print(f"Net salary: {net_salary:.2f}")

except ValueError:
    print("Invalid input. Please enter valid numbers.")
