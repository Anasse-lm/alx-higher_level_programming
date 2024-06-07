#!/usr/bin/python3
print(", "
        .join("0{}".format(i) if i < 10 else "{}".format(i) for i in range(0, 100)))
