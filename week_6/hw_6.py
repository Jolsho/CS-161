
# 1, 2, 3
t = int(input("Enter number to count down from: "))
d = int(input("Enter stride length of count down: "))
while t > 0:
    print(f"{t} is {"even" if t % 2 == 0 else "odd"}")
    t -= d

print("BLASTOFF!!")
print()


# 4. words less than 5 letters game
MAX_ATTEMPTS = 5
GOAL = 5
tries = 0
current = GOAL
while tries < MAX_ATTEMPTS and current >= GOAL:
    tries += 1
    word = input("Enter a word: ")
    current = len(word)
    print(f"{word} has {current} letters.")

if current < GOAL:
    print("GOODBYE")
else:
    print("LOSER")
print()


# 5 counting in dec, bin, and hex while loop
i = 10
while i < 100:
    print(f"{i} {bin(i)} {hex(i)}")
    i += 1
print()


# 6 two function that print number of stars
def star_printer_while(count):
    while count > 0:
        print(f"{"*" * count}")
        count -= 1


def star_printer_recursed(count):
    if count > 0:
        print(f"{"*" * count}")
        star_printer_recursed(count - 1)


print("STAR PRINTER WHILE LOOP: ")
star_printer_while(5)
print("STAR PRINTER RECURSION: ")
star_printer_recursed(5)
print()


# EXTRA CREDIT
def recursive_sum(n):
    digit = 0
    if n > 0:
        digit = n % 10
        n = recursive_sum(n // 10)
    return digit + n


numbers = [123, 9875]
for num in numbers:
    print(f"Summed digits of {num} == {recursive_sum(num)}")
print()


def recursive_palindrome_checker(word):
    length = len(word)
    if length > 0:
        if word[0] == word[length - 1]:
            word = word[1:length - 1]
            return recursive_palindrome_checker(word)
        else:
            return False
    return True


words = ["car", "racecar", "madam", "something"]
for word in words:
    if recursive_palindrome_checker(word):
        print(f"YES, '{word}' is a palindrome.")
    else:
        print(f"NO, '{word}' is NOT a palindrome.")
