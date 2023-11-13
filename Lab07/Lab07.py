import numpy as np
import matplotlib.pyplot as plt
import math
import cmath
from scipy.stats import norm

def uniformGen(a, c, m, seed, N):
    x = seed
    u = x/m
    ui = []
    for _ in range(18):
        x = (a*x + c)%m
        u = x/m
        ui.append(u)

    for _ in range(17, N):
        ui.append(ui[-17] - ui[-5])
        if(ui[-1] < 0):
            ui[-1] += 1
    return ui

def yi(u):
    return np.exp(np.sqrt(u)) + np.exp(np.sqrt(1-u))

cases = [100, 1000, 10000, 100000]

print("<------- Simple Monte Carlo Estimator -------->")
simpleRes = []
# Simple estimator:
for N in cases:
    Y = list()
    ui = uniformGen(256, 654, 244944, 69, N)
    for i in range(N):
        Y.append(math.exp(math.sqrt(ui[i])))

    mean = np.mean(Y)
    var = np.var(Y)
    delta = norm.ppf((1-0.95)/2)
    l = mean + (delta*math.sqrt(var))/np.sqrt(N)
    r = mean - (delta*math.sqrt(var))/np.sqrt(N)
    simpleRes.append((l, r))
    print(f"For {N} samples: Mean: {mean:0,.6f}, 95% confidence interval: [{l:0,.6f}, {r:0,.6f}], width: {r-l:0,.6f}")

print("")
anthRes = []
# Antithetic:

print("<------- Antithetic Estimator -------->")
for num in cases:
    ui = uniformGen(1597, 345, 244944, 23, num)
    Im = 0
    curr = math.floor(num/2)
    Y = []
    for i in range(num):
        Y.append(yi(ui[i])/2)
    Im = np.mean(Y)
    var = 0
    ui = np.array(ui[:curr])
    var = np.var(Y)
    delta = norm.ppf((1-0.95)/2)
    l = Im+(delta*math.sqrt(var)/math.sqrt(curr))
    r = Im-(delta*math.sqrt(var)/math.sqrt(curr))
    anthRes.append((l, r))
    print(f"For {num} samples: Mean: {Im:0,.6f}, 95% confidence interval: [{l:0,.6f}, {r:0,.6f}], width: {r-l:0,.6f}")

print("")

for i in range(4):
    print(f"For {cases[i]} samples: the ratio of 95% condifdence intervals is {(simpleRes[i][1]-simpleRes[i][0])/(anthRes[i][1]-anthRes[i][0]):0,.6f}")