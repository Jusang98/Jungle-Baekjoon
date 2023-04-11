import sys
import math

condition = list(map(int, sys.stdin.readline().split()))

A = condition[0] 
B = condition[1] 
V = condition[2] 
days = (V - B) / (A - B)  

print(math.ceil(days)) 