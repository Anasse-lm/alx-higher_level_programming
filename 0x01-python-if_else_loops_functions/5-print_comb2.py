#!/usr/bin/python3
#for i in range(0,99):
    #if (i < 10):
        #print("0{}".format(i), end=", ")
    #else:
        #print("{}".format(i), end=", ")
print(", ".join(
    "0{}".format(i) if i < 10 else "{}".format(i) for i in range(0, 100)
))
