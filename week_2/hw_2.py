
# DATA STORAGE CONTINUED #####################################

# 1. printing out a variable first in binary then in hex
x = 32
print(x, bin(x), hex(x))

# 2. if I were to instead set x = 1.8
# I would get a TypeError because bin() and hex() expect an integer
# and 1.8 is of type float


# 3. Assigning binary and hex values to variables
y = 0b1011
z = 0xA3
print(y, z)


# 4. Adding numbers in different representations
w = x + y + z
print('SUM:: ', w)


# COMPRESSION #####################################
original_size = 240
dictionary_size = 25
compressed_text_size = 148
total = compressed_text_size + dictionary_size
compress_percent = 1 - (total / original_size)

print(f"Compressed text size: {compressed_text_size} characters")
print(f"     Dictionary size: {dictionary_size} characters")
print(f"               Total: {total} characters")
print(f"  Original text size: {original_size} characters")
print(f"         Compression: {compress_percent * 100}%")


# EXTRA CREDIT #####################################
def twos_compliment(arr) -> list[int]:
    compliment = [0] * len(arr)

    # derive Ones compliment of number
    for i in range(len(arr)):
        if arr[i] == 0:
            compliment[i] = 1
        else:
            compliment[i] = 0

    # derive Twos compliment of number by adding one
    carry = 1
    for i in range(len(arr) - 1, -1, -1):
        if compliment[i] == 1 and carry == 1:
            compliment[i] = 0

        elif carry == 1:
            compliment[i] = 1
            carry = 0

    return compliment


number_in = int(input("Enter a number: "))
if number_in < -128 or number_in > 127:
    print("Invalid number size, must be between -128 & 127.")

else:
    # remove prefix and fill from left with 0's
    binary_str = ""
    if number_in < 0:
        binary_str = bin(number_in)[3:]
    else:
        binary_str = bin(number_in)[2:]
    binary_str = binary_str.zfill(8)

    arr = [0] * 8

    # convert to list of numbers
    for i, b in enumerate(binary_str):
        if binary_str[i] == "0":
            arr[i] = 0
        else:
            arr[i] = 1

    # if negative print twos compliment
    # else print regular binary representation
    if number_in < 0:
        compliment = twos_compliment(arr)
        print(f"Twos Compliment of {number_in} == {compliment}")
    else:
        print("Number is already positive leaving as is...")
        print(f"{number_in} == {arr}")
