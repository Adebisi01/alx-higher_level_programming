#!/usr/bin/python3
def remove_char_at(str, n):
    string = str
    if n < 0:
        return string
    elif len(string) >= n:
        return string
    else:
        newString = string.replace(string[n], '')
        return newString
