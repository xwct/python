#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calc(val):
    return val[0]*val[1]*val[2], val[0]*val[1]


def getinput():
    e, t, h = [int(i) for i in input().split(" ")]
    h = float(h)/100
    return e-1, t, h

print("skriv antall etasjer, antall trinn/etasje, og høyden på hvert trinn i cm, separert med mellomrom")
meter, trinn = calc(getinput())
print(meter, "meter og", trinn, "trinn totalt")
