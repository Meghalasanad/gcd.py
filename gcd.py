#!/bin/python
"""
gcd.py
Tim Vergenz

Calculates gcd-related things for CS 2051.  Output looks best for a,b < 1000.
"""

def calc_gcd(a, b):
    """
    Calculate the gcd of a and b.

    Returns a tuple of (gcd,table) where gcd is the result and table is a list
    of tuples (a,b,q,r) for each recursive step, such that a = b*q + r.
    """
    assert a >= b and a > 0 and b > 0
    r = a % b
    q = (a-r)/b

    if r == 0:
        return b,[]
    else:
        gcd,table = calc_gcd(b, r)
        table = [(a,b,q,r)] + table
        return gcd,table

def calc_xy(a, b, table, sofar=None):
    """
    Calculate x and y for the given gcd calculation for a and b such that
      a*x + b*y == gcd(a,b)
    """
    if sofar is None:
        sofar = [(a,1,0),(b,0,1)]

    if len(table) == 0:
        return sofar[-1][1:]
    else:
        _,_,q,r = table[0]
        (_,xa,ya),(_,xb,yb) = sofar[-2:]
        (x,y) = (xa - q*xb, ya - q*yb)
        print '%3d = (%d*%d + %d*%d) - %d*(%d*%d + %d*%d)' % (r,a,xa,b,ya,q,a,xb,b,yb)
        print '    = %d*%d + %d*%d' % (a,x,b,y)
        sofar += [(r,x,y)]
        return calc_xy(a, b, table[1:], sofar)

if __name__=='__main__':
    a = int(raw_input('a? '))
    b = int(raw_input('b? '))

    gcd,table = calc_gcd(a,b)
    print '(%d,%d) = %d' % (a,b,gcd)
    print
    print 'Table:'
    for _a,_b,q,r in table:
        print ' %3d = %3d x %3d + %d' % (_a,_b,q,r)
    print
    calc_xy(a,b,table)

