#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def negative():
    print("Отрицательное")

def positive():
    print("Положительное")

def test():
    num = int(input("Введите целое число: "))
    if num > 0:
        positive()
    elif num < 0:
        negative()

if __name__ == '__main__':
    test()
