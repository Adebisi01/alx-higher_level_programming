#!/usr/bin/python3
import sys
def main():
    if len(sys.argv) == 0:
        print("0 arguments{}".format(''))
    elif len(sys.argv) == 1:
        print("{} argument:".format(1))
        print("{}: {}".format(1, sys.argv[0]))
    else:
        print("{} arguments:".format(len(sys.argv)))
    for i in range(0, len(sys.argv)):
        print("{}: {}".format(i, len(sys.argv)))

if __name__ == "__main__":
    main()
