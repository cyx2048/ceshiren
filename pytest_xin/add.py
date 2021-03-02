# -*- coding: utf-8 -*-
# @Time    : 2021/3/2 20:57
# @Author  : cyx
# @function: l = [10,3,6,5,4] 算出每一天的值

l = [10,3,6,5,4]
lout = [l[0]]
i = 0
for i in range(1,len(l)):
    a=l[i]-l[i-1]
    lout.append(a)
print(lout)
for j in range(len(lout)):
    print(lout[j])






# print(list(range(6)))
