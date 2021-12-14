#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def first(tip):
    def second(spisok):
        if tip == list:
            return list(map(int, spisok.split()))
        return tuple(map(int, spisok.split()))

    return second


if __name__ == "__main__":
    print(first(list)('1 2 3 4 5 6 7 8 9'))
    print(first(tuple)('1 2 3 4 5 6 7 8 9'))
