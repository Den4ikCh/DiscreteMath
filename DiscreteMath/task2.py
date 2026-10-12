from sympy import *

n = symbols('n', integer=True)
a, b, c = 2, 16, -32
d = lambda k: k * 7**k

r = symbols('r')
print("Корни:", roots(r**3 - a*r**2 - b*r - c, r))   # {2:1, 4:1, -4:1}

A, B = symbols('A B')
fp = lambda k: (A*k + B) * 7**k
eq = expand((fp(n+3) - a*fp(n+2) - b*fp(n+1) - c*fp(n) - d(n)) / 7**n)
sol = solve([eq.coeff(n, 1), eq.coeff(n, 0)], [A, B])
print("A, B =", sol)                                  # 1/165, -721/27225

C1, C2, C3 = symbols('C1 C2 C3')
f = lambda k: (C1*2**k + C2*4**k + C3*(-4)**k
               + (sol[A]*k + sol[B]) * 7**k)
cs = solve([f(0) - 1, f(1) - 2, f(2) - 3], [C1, C2, C3])
print("C =", cs)                                      # 53/50, -1/72, -19/968
F = lambda k: f(k).subs(cs)

seq = [1, 2, 3]
for k in range(3):
    seq.append(a*seq[k+2] + b*seq[k+1] + c*seq[k] + d(k))
print("По рекурренте:", seq[:5])
print("По формуле:   ", [F(k) for k in range(5)])