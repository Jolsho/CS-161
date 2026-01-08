from datetime import datetime
import calendar


def validate_int_n_execute(value, callback):
    try:
        int_value = int(value)
        callback(int_value)
    except (TypeError, ValueError):
        print("You didn't enter a number...\n")


pet_type = "dog"
pet_name = "Ben"

print(f"I have a {pet_type} and his name is {pet_name}.")

first_name = input("Enter your first name: ")
age = input("Enter your current age: ")
savings = input("Enter your yearly savings: ")

print(f"Hello {first_name}! You are currently {age} years old.")
validate_int_n_execute(age, lambda int_age: print(f"In 10 years you will be {int_age + 10} years old."))


def print_savings(int_savings):
    print(f"If you save ${int_savings} each year, in 5 years you will have saved ${int_savings * 5}")
    print(f"Your average monthly savings is ${int_savings // 12}")


validate_int_n_execute(savings, print_savings)


year = datetime.now().year
days_in_jan = calendar.monthrange(year, 1)[1]
secs_in_jan = days_in_jan * 24 * 60 * 60
print(f"The number of seconds in January is {secs_in_jan}")

egg_count = input("Enter the number of eggs: ")
validate_int_n_execute(egg_count, lambda eggs: print(f"This makes {eggs // 12} dozen eggs with {eggs % 12} left over."))
