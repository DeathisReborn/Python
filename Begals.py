#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/6 15:23
# @Author  : DeathIsReborn
# @File    : Begals.py
# @Software: PyCharm
import random

# 定义数字的个数
NUM_DIGITS = 3
# 定义猜测的次数
MAX_GUESS = 10


def getSecretNum():
    # 返回一个由 NUM_DIGITS 个不重复随机数组成的字符串
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    # 返回一个由 Pico, Fermi 和 Bagels 组成的，用来提示用户的字符串
    if guess == secretNum:
        return '恭喜你,猜对了!'
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    clues.sort()
    return ' '.join(clues)


def isOnlyDigits(num):
    # 如果字符串只包含数字，返回真。否则返回假
    if num == '':
        return False
    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False
    return True


print('我在想一个%s位数,试着猜猜是什么.' % NUM_DIGITS)
print('我提供的线索是...')
print('当我说:    那意味着:')
print('  Bagels       所有数字都不正确.')
print('  Pico         一个数字是正确的,但位置不对.')
print('  Fermi        一个数字正确且位置正确.')

while True:
    secretNum = getSecretNum()
    print('我想出了一个数字,你有%s个猜测.' % MAX_GUESS)
    guessesTaken = 1
    while guessesTaken <= MAX_GUESS:
        guess = ''
        while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
            print('Guess #%s: ' % guessesTaken)
            guess = str(input())
        print(getClues(guess, secretNum))
        guessesTaken += 1
        if guess == secretNum:
            break
        if guessesTaken > MAX_GUESS:
            print('你猜不出来了,答案是%s.' % secretNum)
    print('你想再玩一次吗?（是或否）?')
    if not input().lower().startswith('是'):
        break
