import sys
count = int(sys.argv[1])
[print("{0: >{1}}".format('#'*(x+1), count)) for x in range(count)]