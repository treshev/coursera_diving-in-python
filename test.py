def count_sub(sub, string):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count += 1
        else:
            return count


string = 'AMAMAMAMAMAMAMAAA'
string2 = string[::-1]
s = 'AMA'

print("String length = {}".format(len(string)))
print("Method 1 str.count =              {}".format(string.count(s)))
print("Method 2 str.count + str2.count = {}".format(string.count(s) + string2.count(s)))
print("Method 3 substring function     = {}".format(count_sub(s, string)))

L1 = [1,2]
L2 = [3,4]
print(dict(map(lambda x: x, zip(L1, L2))))