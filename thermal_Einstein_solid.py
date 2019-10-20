#coding:utf-8
import itertools
import time
import math
 
#使用permutations方法
N = int(input("number of N:"))
q = int(input("number of q:"))

list = []
for num in range(0, 100):
	list.append(num)
ls = itertools.product(list, repeat = N)
 
#遍历所有组合情况
for l in ls:
    if(math.fsum(l) != q):
        continue
    else:
        print (l)
	
time.sleep(1500);