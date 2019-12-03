#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/3 13:27
# @Author  : DeathIsReborn
# @File    : jump7.py
# @Software: PyCharm

num = 0
while num < 100:
    num += 1
    if num % 7 == 0:
        continue
    elif num % 10 == 7 or num // 10 == 7:
        continue
    print (num)
