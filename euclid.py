import sys

if len(sys.argv)<3:
    sys.exit("expected TWO parameters")

param_a = int(sys.argv[1])
param_b = int(sys.argv[2])

def substract(a, b):
    """Finds the GCD using the Euclidean algorithm.
    https://en.wikipedia.org/wiki/Euclidean_algorithm"""
    b_init = b
    times=0
    remainder = 0
    while(b>=a):
        b=b - a
        times += 1
        if a>b:
            remainder = b

    if remainder >0:
         return substract(remainder, a)
    else:
        return a


if param_a>param_b:
    a_s=param_a
    param_a=param_b
    param_b=a_s
res = substract(param_a, param_b)
print("the GCD of {a} and {b} is {gcd}".format(a = param_a, b=param_b, gcd=res))

