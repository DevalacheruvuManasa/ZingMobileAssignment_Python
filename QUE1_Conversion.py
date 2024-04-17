'''Decimal to Hexa, Hexa to Decimal conversion
a. Validate the input if it’s not in decimal format print invalid input, convert to
hexadecimal
b. Do it vise-versa
Note: don’t use in-built functions'''

def is_valid_decimal(num):
    """Check if the input is a valid decimal number."""
    try:
        int(num)
        return True
    except ValueError:
        return False

def decimal_to_hexa(num):
    """Convert a decimal number to hexadecimal."""
    if not is_valid_decimal(num):
        print("Invalid input. Please enter a valid decimal number.")
        return
    hexa = hex(int(num)).split('x')[-1]
    print(f"The hexadecimal representation of {num} is: {hexa.upper()}")

def is_valid_hexa(num):
    """Check if the input is a valid hexadecimal number."""
    hex_digits = set('0123456789ABCDEFabcdef')
    if len(num) % 2 != 0:
        return False
    for i in range(0, len(num), 2):
        if num[i:i+2] not in hex_digits:
            return False
    return True

def hexa_to_decimal(hexa):

    if not all(c in "0123456789abcdefABCDEF" for c in hexa):

        return "Invalid input"

    decimal = 0

    hexa_len = len(hexa)

    for i, c in enumerate(hexa[::-1]):

        if c >= 'a' and c <= 'f':

            digit = ord(c) - ord('a') + 10

        elif c >= 'A' and c <= 'F':

            digit = ord(c) - ord('A') + 10

        else:

            digit = int(c)

        decimal += digit * (16 ** i)

    return decimal

# Example usage
inp=input("enter the decimal value:");
decimal_to_hexa(inp)
inp1=input("enter the hexadecimal value:");
print("decimal value is:",hexa_to_decimal(inp1))