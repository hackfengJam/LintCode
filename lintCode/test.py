#!/usr/bin/env python
# coding=utf-8


def text_str():
    test = "01234"
    print [int(x) for x in test]


def text_sort():
    text = [12, 3, 11, 3, 4, 1]
    print sorted(text)
    print text


if __name__ == '__main__':
    # text_str()
    text_sort()