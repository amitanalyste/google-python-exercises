#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 12:41:07 2017

@author: amit
"""
import sys, re

def solution(lst):
  length = len(lst)
  oddList = []
  evenList = []
  for i in range(length):
      if i % 2 == 1:
          oddList.append(list[i])
      else:
          evenList.append(list[i])
  return oddList
def createList(string):
  #print("createList")
  return re.findall('(\w)\W', string)
          

def main():
  argument = sys.argv[1:][0]
  print(argument)
  x = createList(argument)
  #for a in argument:
   #   print(a)
  print(solution(x))
  #print(lst.split())
  #print(type(lst))
#==============================================================================
#   if len(sys.argv) > 2:
#       print("Program is considering only first input")
#   if type(lst) is list:
#       oddList = solution(lst)
#       return oddList
#   else:
#       print("Input is not a List!")
#==============================================================================
  

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()