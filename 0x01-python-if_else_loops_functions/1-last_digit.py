#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = int(str(number)[-1])
print(f"Last digit of {number} is {last} and ", end='')
if last < 0:
    last = last * -1
else:
    last = last
if last > 5:
    print("is greater than 5")
elif last == 0:
    print("is 0")
elif last < 6 & last != 0:
    print("is less than 6 and not 0")
