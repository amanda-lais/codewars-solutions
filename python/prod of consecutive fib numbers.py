# Given a number, say prod (for product), we
# search two Fibonacci numbers F(n) and F(n+1) verifying
# F(n) * F(n+1) = prod.

def fib(n,p):
    if n >= len(p):
        p.append(fib(n-1,p)[0] + fib(n-2,p)[0])
    return [p[n],p]

def product_fib(_prod):
    prev_f = [0,1]
    prod, xi = 0,0
    while prod <= _prod:
        prev_f = fib(xi+1, prev_f)[1]
        x = prev_f[xi]
        y = prev_f[xi+1]
        prod = x * y
        if prod == _prod: return [x, y, True]
        xi += 1
    prev_f = fib(xi, prev_f)[1]
    x = prev_f[xi-1]
    y = prev_f[xi]
    return [x, y, False]