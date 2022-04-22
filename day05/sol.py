#!/usr/bin/python3

import sys
import itertools
import re


def gcd(a,b):
    if a == 0:
        return b
    if b%a == 0:
        return a
    return gcd(a, b%a)

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def sub(self, v):
        return vector(self.x - v.x, self.y - v.y)
    def __repr__(self):
        return f'point({self.x},{self.y})'
    def __str__(self):
        return f'({self.x},{self.y})'
    def __hash__(self):
        return self.x * 10007 + self.y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __sub__(self, other):
        return self.sub(other)

class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def dot(self, v):
        return self.x * v.x + self.y * v.y
    def parallel(self, v):
        return self.x * v.y - self.y * v.x == 0
    def normalize(self):
        if(self.dot(self) == 0):
            return self
        gcf = abs(gcd(self.x, self.y))
        return vector(self.x//gcf, self.y//gcf)
    def perp(self):
        return vector(-self.y, self.x)
    def plus(self, p):
        return point(self.x + p.x, self.y + p.y)
    def times(self, m):
        return vector(self.x * m, self.y * m)
    def __rerp__(self):
        return f'vector({self.x},{self.y})'
    def __str__(self):
        return f'({self.x},{self.y})'
    def __add__(self, other):
        return self.plus(other)
    def __mul__(self, other):
        if isinstance(other, vector):
            return self.dot(other)
        return self.times(other)

class line:
    def __init__(self, p1, p2):
        self.start = p1
        self.end = p2
        self.vec = p2 - p1
        self.mag = self.vec * self.vec
        self.dir = self.vec.normalize()
        self.norm = self.dir.perp()
    def intersection(self, l):
        if self.dir.parallel(l.dir):
            return self._parallel_intersection(l)
        else:
            return self._nonparallel_intersection(l)
    def _nonparallel_intersection(self, l):
        v = self.start - l.start
        vperp = -(v * l.norm)
        dperp = self.dir * l.norm
        if vperp % dperp != 0:
            return set() 
        t = vperp // dperp
        inter = self.dir * t + self.start
        vec = inter - self.start 
        mag = vec * self.vec
        if mag < 0 or mag > self.mag:
            return set()
        vec = inter - l.start
        mag = vec * l.vec
        if mag < 0 or mag > l.mag:
            return set()
        return {inter}
    def _parallel_intersection(self, l):
        ret = set()
        v = l.start - self.start
        if not v.parallel(l.dir):
            return ret
        w = l.end - self.start
        s = v * self.dir
        t = w * self.dir
        if s > t:
            s,t = t,s
        s = max(0, s)
        t = min(t, self.vec * self.dir)
        u = self.dir * self.dir
        p = self.dir * (s // u) + self.start
        while(s <= t):
            ret.add(p)
            s += u
            p = self.dir + p
        return ret
    def __repr__(self):
       return f'line({repr(self.start)},{repr(self.end)})'
    def __str__(self):
       return f'{self.start} -> {self.end}'


lines = []
f = open('input', 'r')
regex = re.compile(r"(\d+),(\d+)\s*->\s*(\d+),(\d+)")
for l in f:
    res = regex.match(l)
    if not res:
        print(f'couldn\'t match: {l}')
    else: 
        ln = line(point(int(res[1]), int(res[2])), point(int(res[3]), int(res[4])))
    if ln.vec.x * ln.vec.y != 0:
        # continue
        pass
    lines.append(ln)

res = set()
for i in range(len(lines)):
    for j in range(i+1, len(lines)):
        res |= lines[i].intersection(lines[j])

print(len(res))
