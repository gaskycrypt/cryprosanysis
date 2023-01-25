def h(n):
    return hex(n).replace("0x","")

def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m
    
N = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141


K = 0x7fffffffffffffffffffffffffffffff5d576e7357a4501ddfe92f46681b20a0
R = 0x5d8e2220f7f741919417a5105e6efec6ea3918600980deb26d5b4cecc83998be
S = 0xdc319b3c61f6ffe5963364019f5da1127ef7438a9a83537f50b92d49037c2f6f
Z = 0x58190c538f579759a777dc93fb5c522e5281e7ceb63f3322f753e9e34e399d32

print (h((((S * K) - Z) * modinv(R,N)) % N))
