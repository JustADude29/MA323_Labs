import numpy as np
import math
from scipy.stats import norm

def linGen(a,b,m,seed,N):
    res = []
    x = seed
    u = x/m

    for _ in range(1, 18):
        x = (a*x + b)%m
        u = x/m
        res.append(u)

    for i in range(18, N+1):
        x = res[i-17] - res[i-5]
        if(x<0): x+=1
        res.append(x)
    return res


def monte_carlo_estimate(N):
    Y = list()
    ui = linGen(256, 654, 244944, 69, N)
    for i in range(N):
        Y.append(math.exp(math.sqrt(ui[i])))

    mean = np.mean(Y)
    var = np.var(Y)
    delta = norm.ppf((1-0.95)/2)
    l = mean + (delta*math.sqrt(var))/np.sqrt(N)
    r = mean - (delta*math.sqrt(var))/np.sqrt(N)
    print(f"for M: {M} -> Estimated value: {mean}, variance: {var}, and 95% confidence interval: [{l}, {r}] and width: {r-l:0,.6f}")

M_values = [10**2, 10**3, 10**4, 10**5]

for M in M_values:
    monte_carlo_estimate(M)

print("Exact I = 2 in all cases")
