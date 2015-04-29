import sys

def is_valid(isbn):
    first_9_digits = isbn[:9]
    check_digits = range(10, 1, -1)

    total = 0
    for digit, check_digit in zip(first_9_digits, check_digits):
        total += (int(digit) * check_digit)

    possible_check_digit = (11 - (total % 11)) % 11

    expected_check_digit = "X" if possible_check_digit == 10 else possible_check_digit
    actual_check_digit = isbn[-1:]

    return str(expected_check_digit) == str(actual_check_digit)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: %s <isbn-10>" % sys.argv[0])

    isbn = sys.argv[1]

    if len(isbn) != 10:
        sys.exit("ERROR: ISBN should be 13 digits long")

    if is_valid(isbn):
        print "Valid"
    else:
        sys.exit("Invalid isbn check digit")
