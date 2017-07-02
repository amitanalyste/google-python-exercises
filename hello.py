#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""A tiny Python program to check that Python is working.
Try running this program from the command line like this:
  python hello.py
  python hello.py Alice
That should print:
  Hello World -or- Hello Alice
Try changing the 'Hello' to 'Howdy' and run again.
Once you have that working, you're ready for class -- you can edit
and run Python code; now you just need to learn Python!
"""

import sys

# Define a main() function that prints a little greeting.
def solution(lst):
  oddList = []
  count = -1
  for item in lst:
    count += 1
    if count %2 == 1:
      oddList.append(item)
      
  return oddList

def solution2(number):
  digits = [int(x) for x in str(number)]
  return digits

def main():
  # Get the name from the command line, using 'World' as a fallback.
  #print("AMit")
  if len(sys.argv) >= 2:
    name = sys.argv[1]
  else:
    name = 'World'
  print('Hello', name)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
def map(s):
    op = {}
    for word in s:
        if word in op:
            return False
        else:
            op[word] = 1
    return True
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    lols = (s[0], 1)
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if(map(s[i:j]) and (j-i) > lols[1]):
                lols = (s[i:j], j-i)
    return lols[0]