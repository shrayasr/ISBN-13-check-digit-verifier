import sys

if len(sys.argv) < 2:
    sys.exit("Usage: %s <isbn-13>" % sys.argv[0])

isbn = sys.argv[1]

if len(isbn) != 13:
    sys.exit("ERROR: ISBN should be 13 digits long")

first_12_digits = list(isbn)[:12]

digit_sum = 0
for idx, digit in enumerate(first_12_digits):
    digit = int(digit)
    idx = idx+1
    if idx % 2 == 0:
        digit_sum += digit * 3
    else:
        digit_sum += digit

reminder = digit_sum % 10
check_digit = (10 - reminder) % 10

expected_isbn = "%s%s" % ("".join(first_12_digits), check_digit)
actual_isbn = isbn

if (actual_isbn == expected_isbn):
    print "Valid"
else:
    sys.exit("ERROR: Expected %s as the check digit" % check_digit)

