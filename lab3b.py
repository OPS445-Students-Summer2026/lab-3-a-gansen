#!/usr/bin/env python3
'''Lab 3 Part 1 script - functions'''
# Author ID: agansen

def sum_numbers(number1, number2):
    number3 = int(number1) + int(number2)
    return number3

def subtract_numbers(number1, number2):
    number3 = int(number1) - int(number2)
    return number3

def multiply_numbers(number1, number2):
    number3 = int(number1) * int(number2)
    return number3

if __name__ == '__main__':
    print(sum_numbers(10, 5))
    print(subtract_numbers(10, 5))
    print(multiply_numbers(10, 5))