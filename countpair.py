# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 10:31:02 2019

@author: supriya
"""
from collections import Counter
def findPairs( nums, k):
        pairs = 0
        c = Counter(nums)
        for i in c:
            if k > 0 and i + k in c or k == 0 and c[i] > 1:
                pairs += 1
        return pairs
nums = [int(x) for x in input().split()]
k=int(input())
a=findPairs(nums, k)
print(a)