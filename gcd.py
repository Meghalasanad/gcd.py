#!/bin/python
"""
gcd.py
Tim Vergenz

Calculates gcd-related things for CS 2051.  Output looks best for a,b < 1000.

Example output:

    $ python gcd.py
    a? 777
    b? 652
    (777,652) = 1

    Table:
     777 = 652 x   1 + 125
     652 = 125 x   5 + 27
     125 =  27 x   4 + 17
      27 =  17 x   1 + 10
      17 =  10 x   1 + 7
      10 =   7 x   1 + 3
       7 =   3 x   2 + 1

    125 = (777*1 + 652*0) - 1*(777*0 + 652*1)
        = 777*1 + 652*-1
     27 = (777*0 + 652*1) - 5*(777*1 + 652*-1)
        = 777*-5 + 652*6
     17 = (777*1 + 652*-1) - 4*(777*-5 + 652*6)
        = 777*21 + 652*-25
     10 = (777*-5 + 652*6) - 1*(777*21 + 652*-25)
        = 777*-26 + 652*31
      7 = (777*21 + 652*-25) - 1*(777*-26 + 652*31)
        = 777*47 + 652*-56
      3 = (777*-26 + 652*31) - 1*(777*47 + 652*-56)
        = 777*-73 + 652*87
      1 = (777*47 + 652*-56) - 2*(777*-73 + 652*87)
        = 777*193 + 652*-230
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

def calc_xy(a, b, table, sofar=None):#function definition
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

