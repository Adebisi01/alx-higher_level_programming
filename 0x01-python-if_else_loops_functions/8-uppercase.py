#!/usr/bin/python3
def uppercase(charac):
    for i in range(0, len(charac) + 1):
        if charac[i] >= 97 and charac[i] <= 122:
            char = ord(charac[i]) + 32
        else:
            char = ord(charac[i])
        print("{}".format(chr(char)), end='')