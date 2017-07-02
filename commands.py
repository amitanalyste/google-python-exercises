#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 15:50:37 2017

@author: amit
"""

import sys, subprocess

def List(dir):
    cmd = 'ls -l ' + dir
    print(cmd)
    (status, output) = subprocess.getstatusoutput(cmd)
    
    print(status)
    if status != 0:
        sys.stderr.write('There was an error: ', output)
        sys.exit(1)
    else:
        print(output)
    
#    filenames = os.listdir(dir)
#    print(filenames)
#    for filename in filenames:
#        path = os.path.join(dir, filename)
#        #print(path)
#        print(os.path.abspath(path))
    
    
        
def main():
    List(sys.argv[1])


if __name__ == '__main__':
    main()