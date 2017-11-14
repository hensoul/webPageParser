#!/usr/bin/env python
# coding: utf-8
import numbers


class BaseUtil(object):

    @staticmethod
    def format_number(number):
        if isinstance(number, int) or isinstance(number, numbers.Integral):
            return number
        else:
            if number is None:
                return 0

            if len(number.strip()) == 0:
                return 0
            number = number.replace('(', '')
            number = number.replace(')', '')
            number = number.replace(',', '')
            number = number.replace(' ', '')
            ten_thousand = unicode('万', 'utf-8')
            hundred_million = unicode('亿', 'utf-8')
            if number.find(ten_thousand) != -1:
                number = number.replace(ten_thousand, '')
                return float(number) * 10000
            elif number.find(hundred_million) != -1:
                number = number.replace(hundred_million, '')
                return float(number) * 100000000
            else:
                return number
