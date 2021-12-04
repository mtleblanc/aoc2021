#!/usr/bin/python3

import sys
import itertools

f = open("input", "r")

def list2bin(ls):
    res = 0
    for l in ls:
        res *= 2
        res += l
    return res

def str2list(s):
    t = s.strip()
    return [int(d) for d in t]

def mostCommonBinary(ls):
    return 1 if 2*sum(ls)>=len(ls) else 0

def gammaEpsilon(ls):
    gamma = [mostCommonBinary([c[i] for c in ls]) for i in range(len(ls[0]))]
    epsilon = [1-c for c in gamma]
    return list2bin(gamma), list2bin(epsilon)

def filterOn(ls, index, criteria):
    keep = criteria([c[index] for c in ls])
    return [c for c in ls if c[index] == keep]

def __main__():
    f = open("input", "r")
    ls = [str2list(l) for l in f]
    gamma, epsilon = gammaEpsilon(ls)
    print(f'Gamma: {gamma}, Epsilon: {epsilon}, Power Consumption: {gamma*epsilon}')

    oxygenList = ls
    index = 0
    while(len(oxygenList) > 1):
        oxygenList = filterOn(oxygenList, index, mostCommonBinary)
        index += 1
    oxygen = list2bin(oxygenList[0])

    carbonDioxideList = ls
    index = 0
    while(len(carbonDioxideList) > 1):
        carbonDioxideList = filterOn(carbonDioxideList, index, lambda x: 1 - mostCommonBinary(x))
        index += 1

    carbonDioxide = list2bin(carbonDioxideList[0])
    print(f'Oxygen: {oxygen}, Carbon Dioxide: {carbonDioxide}, Life Support: {oxygen*carbonDioxide}')

__main__()
