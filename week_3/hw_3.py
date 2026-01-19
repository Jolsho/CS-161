name = input("Enter your name: ")
print("Hello " + str(name))


# input() output is of type string so we must convert to int
# in order to be able to do arithmetic with it
# this could raise a type error if they dont enter an int
# but that is outside the scope of this assignment
age = int(input("Enter your age: "))
delta = int(input("Enter an age delta: "))
age += delta
print("In " + str(delta) + " years you will be " + str(age) + " years old")


# tax table with tuple (min, max, tax_rate)
# last entry max is largest integer
tax_table = [
    (0, 11_600, 0.10),
    (11_600, 47_150, 0.12),
    (47_150, 100_525, 0.22),
    (100_525, 191_950, 0.24),
    (191_950, 243_725, 0.32),
    (243_725, 609_350, 0.35),
    (609_350, 2**31 - 1, 0.37),
]
work_weeks_per_year = 50

hours = float(input("Enter number of hours worked: "))
wage = float(input("Enter an hourly wage without $: "))

estimated_annnual_income = hours * work_weeks_per_year * wage

print("Your gross pay this week is $" + str(hours * wage))
print("Your estimated annual gross income is $" + str(estimated_annnual_income))

# linear search tax table for appropriate tax rate
for min, max, rate in tax_table:
    if estimated_annnual_income >= min and estimated_annnual_income < max:
        print("Estimated net income: $" + str(estimated_annnual_income * (1 - rate)))
