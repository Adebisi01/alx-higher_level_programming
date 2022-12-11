#!/usr/bin/python3
def remove_char_at(str, n):
    newString = str
    newString.replace(str[n], '')
    return newString
