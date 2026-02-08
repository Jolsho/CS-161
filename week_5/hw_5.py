import requests
import psutil


def divisible_by_5(num):
    if (num % 5 == 0):
        print(f"{num} is divisible by 5")
    else:
        print(f"{num} is NOT divisible by 5")


states = {
    "Oregon": "Salem",
    "Washington": "Olympia",
    "Idaho": "Boise",
    "Wisconsin": "Madison",
    "Colorado": "Denver",
    "New York": "Albany",
}


def if_else_states(state):
    if (state == 'Wisconsin'):
        print('Madison')
    elif (state == 'Colorado'):
        print('Denver')
    elif (state == 'Oregon'):
        print('Salem')
    elif (state == 'Washington'):
        print('Olympia')
    elif (state == 'Idaho'):
        print('Boise')
    elif (state == 'New York'):
        print('Albany')
    else:
        print('I do not know that one')


def mapping_states(state):
    if (state in states):
        print(states[state])
    else:
        print('I do not know that one')


def matching_states(state):
    match state:
        case 'Wisconsin':
            print('Madison')
        case 'Colorado':
            print('Denver')
        case 'Oregon':
            print('Salem')
        case 'Washington':
            print('Olympia')
        case 'Idaho':
            print('Boise')
        case 'New York':
            print('Albany')
        case _:
            print('I do not know that one')


def pool_admission_cost(age):
    if (age < 2):
        return 0
    elif (age < 12):
        return 3
    elif (age < 61):
        return 6
    else:
        return 4


def determine_hugo_word_count():
    link = "https://gohugo.io"
    keyword = "Hugo"

    r = requests.get(link)
    exit_code = r.status_code
    if (r.status_code == 200):
        exit_code = 0
        count = 0
        for word in r.text.split(" "):
            if (keyword in word):
                count += 1
        print(f"The substring '{keyword}' appears {count} times" +
              f" in the HTML source of {link}.")

    print(f"Process finished with exit code {exit_code}")


def determine_number_of_processes():
    exit_code = 0
    count = 0
    for process in psutil.process_iter():
        count += 1
    print(f"Number of processes running is {count}")
    print(f"Process finished with exit code {exit_code}")


def main():
    divisible_by_5(int(input("Enter a number: ")))

    state = input("Enter name of a State/Providence: ")
    if_else_states(state)
    mapping_states(state)
    matching_states(state)

    age = int(input("Enter your age: "))
    print(f"Admission to the pool costs ${pool_admission_cost(age)}")

    determine_hugo_word_count()
    determine_number_of_processes()


if __name__ == "__main__":
    main()
