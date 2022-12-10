#!/usr/bin/python3
print("{}".format(str(0).zfill(2)), end='')
for i in range(1, 100):
    print(", {}".format(str(i).zfill(2)), end='')
