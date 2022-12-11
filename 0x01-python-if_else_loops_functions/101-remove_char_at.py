#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    elif len(str) >= n:
        return str
    else:
        newString = str.replace(str[n], '')
        return newString
