# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 17:17:15 2023

@author: rfranco11
"""

numWays = 0 
for p in range(101):
    for n in range(21):
        for d in range(11):
            for q in range(5):
                for h in range(3):
                    if( p + 5*n + 10*d + 25*q + 50*h) == 100:
                        numWays += 1
                        print (p,n,d,q,h)
print(f"\number of ways = {numWays}")