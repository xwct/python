# /usr/bin/python3
# -*- coding: utf-8 -*-
#
# pi calculated by chudonovsky formula

from math import factorial
from decimal import *
import pdb

class pica:
    def __init__(self, rounds, decimals):
        self.iterations = rounds
        self.k = 0
        self.sum1 = 0
        self.t2 = 0
        getcontext().prec = decimals
    def pit(self):
        #pdb.set_trace()
        while self.k < self.iterations:
            #pdb.set_trace()
            self.a = (Decimal(-1)) ** self.k
            self.b = factorial(6 * self.k)
            self.c = (Decimal(545140134) * self.k) + Decimal(13591409)
            self.top = self.a * self.b * self.c
            self.e = (factorial(self.k)) **3
            self.f = factorial(3 * self.k)
            self.g = (Decimal(640320 ** 3)) ** (Decimal(self.k) + Decimal(1 / 2))
            self.bottom = self.e * self.f * self.g
            self.s = Decimal(self.top) / Decimal(self.bottom)
            #self.t = self.s * 12
            #self.sum1 = self.sum1 + self.t
            self.t2 = self.t2 + self.s
            self.sum2 = self.t2 * Decimal(12)
            self.k = self.k + Decimal(1)
            self.inv = 1 / self.sum2
            print(self.k, "\t", self.inv, "\n")


    def test(self, p):
        #pdb.set_trace()
        pica.pit(p)
        
#pdb.set_trace()
if __name__ == '__main__':
    #pdb.set_trace()
    pica.test(10, 100)
