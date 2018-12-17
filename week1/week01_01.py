import sys

digit_string = ""
if len(sys.argv) > 1:
    digit_string = sys.argv[1]

if (digit_string.isdigit()):
    res = 0
    for i in digit_string:
        res +=int(i)
    print(res)
else:
    print("Error. Wrong format! String can be empty and must use only digits!!!")