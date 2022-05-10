import re

test_str = "1sd2nndk9nkd5njd439"

print("The Original String is : ", test_str)

res = ''.join(filter(lambda i: i.isdigit(), test_str))

print("Extracted Digits of a String is: ", res)


numbers = re.findall('[0-9]+', test_str)

print(numbers)

listToStr = ''.join([str(elem) for elem in numbers])

print("combined string is: ",listToStr)