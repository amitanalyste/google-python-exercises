#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 15:50:37 2017

@author: amit
"""

import os, sys

def List(dir):
    filenames = os.listdir(dir)
    print(filenames)
    for filename in filenames:
        path = os.path.join(dir, filename)
        #print(path)
        print(os.path.abspath(path))
    
    
        
def main():
    List(sys.argv[1])


if __name__ == '__main__':
    main()