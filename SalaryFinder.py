print("Today we will help you figure out your net salary"
      "based on your gross income and number of children")

try:
    gross_salary = int(input("Please enter your gross salary: "))
    num_child = int(input("Please enter the number of children you have: "))

## Figure out the tax rate
    if gross_salary < 1000:
        tax_rate = .10
    elif gross_salary < 2000:
        tax_rate = .12
    elif gross_salary < 4000:
        tax_rate = .14
    else:
        tax_rate = .18

## Figure out tax cut based on number of children
    if gross_salary < 2000:
        tax_cut = 0.01 * num_child
    else:
        tax_cut = 0.005 * num_child

## Adjusting the tax rate
    if tax_cut > tax_rate:
        tax_rate = 0
    else:
        tax_rate -= tax_cut

## Calculate the final net salary
    net_salary = round(gross_salary * (1 - tax_rate),2)

## Printing the net salary
    print("After many calculations your net salary is: ", net_salary)
except ValueError:
    print("Please enter valid numbers!")
