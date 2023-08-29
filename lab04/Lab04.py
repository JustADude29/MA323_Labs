import numpy as np
import matplotlib.pyplot as plt
import math
import cmath
import time

def linGen(a, b, m, seed, N):
    res = []
    x = seed
    u = x/m
    for _ in range(N):
        x = (a*x + b)%m
        u = x/m
        res.append(u)
    return res


ranges = linGen(1263, 23, 2385254, 786, 100000)

def BoxMuller(N):
    t1 = time.time()
    res = []
    R = 0
    theta = 0
    z1=0
    i = 0
    u1 = 0
    u2 = 0
    for _ in range(N):
        u1 = ranges[i]
        u2 = ranges[i+1]
        i+=2
        R = math.sqrt(-2*math.log(u1))
        theta = 2*cmath.pi*u2
        z1 = R*math.sin(theta)
        res.append(z1)
    t2 = time.time()
    return res, t2-t1


def MargBray(N):
    t1 = time.time()
    res = []
    i = 0
    rejects = 0
    for _ in range(N):
        u1 = ranges[i]
        u2 = ranges[i+1]
        u1 = 2*u1-1
        u2 = 2*u2-1
        while((u1*u1 + u2*u2)>1):
            i+=2
            rejects+=1
            u1 = ranges[i]
            u2 = ranges[i+1]
            u1 = 2*u1-1
            u2 = 2*u2-1
        i+=2
        u = u1 * math.sqrt((-2*math.log(u1*u1 + u2*u2))/(u1*u1 + u2*u2))
        res.append(u)
    t2 = time.time()
    return res, t2-t1, rejects/(N+rejects)

def Normal(x, mean, var):
    sd = math.sqrt(var)
    return (1/(sd*math.sqrt(2*cmath.pi)))*math.exp((-1/2)*pow((x-mean)/sd, 2))

BM1,BMT1 = BoxMuller(100)
BM2,BMT2 = BoxMuller(10000)

print("Mean of 100 samples generated throught Box Muller method:", np.mean(BM1), "and variance:", np.var(BM1))
print("Mean of 10000 samples generated throught Box Muller method:", np.mean(BM2), "and variance:", np.var(BM2))

MG1,MGT1,rejects1 = MargBray(100)
MG2,MGT2,rejects2 = MargBray(10000)

print("Mean of 100 samples generated throught Margsalia and Bray method:", np.mean(MG1), "and variance:", np.var(MG1))
print("Mean of 10000 samples generated throught Margsalia and Bray method:", np.mean(MG2), "and variance:", np.var(MG2))

# plt.hist(BM1, 100, density=False)
# plt.title("Histogram for BoxMuller method: 100 samples")
# plt.show()


# plt.hist(BM2, 100, density=False)
# plt.title("Histogram for BoxMuller method: 10000 samples")
# plt.show()


# plt.hist(MG1, 100, density=False)
# plt.title("Histogram for Margsalia and Bray method: 100 samples")
# plt.show()


# plt.hist(MG2, 100, density=False)
# plt.title("Histogram for Margsalia and Bray method: 10000 samples")
# plt.show()

# data = np.array(BM1)
# data = data*math.sqrt(5)
# x = np.linspace(-10,10,10000)
# dat2 = [Normal(i, 0, 5) for i in x]
# plt.plot(x, dat2)
# plt.title("Histogram for BoxMuller method: N=100, mean=0, var=5 ")
# plt.hist(data, 100, density=True)
# plt.show()

# data = np.array(BM2)
# data = data*math.sqrt(5)
# x = np.linspace(-10,10,10000)
# dat2 = [Normal(i, 0, 5) for i in x]
# plt.plot(x, dat2)
# plt.title("Histogram for BoxMuller method: N=10000, mean=0, var=5 ")
# plt.hist(data, 100, density=True)
# plt.show()

# data = np.array(MG1)
# data = data*math.sqrt(5)
# x = np.linspace(-10,10,10000)
# dat2 = [Normal(i, 0, 5) for i in x]
# plt.plot(x, dat2)
# plt.title("Histogram for MargsaliaBray method: N=100, mean=0, var=5 ")
# plt.hist(data, 100, density=True)
# plt.show()

# data = np.array(MG2)
# data = data*math.sqrt(5)
# x = np.linspace(-10,10,10000)
# dat2 = [Normal(i, 0, 5) for i in x]
# plt.plot(x, dat2)
# plt.title("Histogram for MargsaliaBray method: N=10000, mean=0, var=5 ")
# plt.hist(data, 100, density=True)
# plt.show()

#----------------------------

# data = np.array(BM1)
# data = data*math.sqrt(5)+5
# x = np.linspace(-10,15,10000)
# dat2 = [Normal(i, 5, 5) for i in x]
# plt.plot(x, dat2)
# plt.title("Histogram for BoxMuller method: N=100, mean=5, var=5 ")
# plt.hist(data, 100, density=True)
# plt.show()

# data = np.array(BM2)
# data = data*math.sqrt(5)+5
# x = np.linspace(-10,15,10000)
# dat2 = [Normal(i, 5, 5) for i in x]
# plt.plot(x, dat2)
# plt.title("Histogram for BoxMuller method: N=10000, mean=5, var=5 ")
# plt.hist(data, 100, density=True)
# plt.show()

# data = np.array(MG1)
# data = data*math.sqrt(5)+5
# x = np.linspace(-10,15,10000)
# dat2 = [Normal(i, 5, 5) for i in x]
# plt.plot(x, dat2)
# plt.title("Histogram for MargsaliaBray method: N=100, mean=5, var=5 ")
# plt.hist(data, 100, density=True)
# plt.show()

# data = np.array(MG2)
# data = data*math.sqrt(5)+5
# x = np.linspace(-10,15,10000)
# dat2 = [Normal(i, 5, 5) for i in x]
# plt.plot(x, dat2)
# plt.title("Histogram for MargsaliaBray method: N=10000, mean=5, var=5 ")
# plt.hist(data, 100, density=True)
# plt.show()

print("Time taken for Box miller for 100 samples:", BMT1)
print("Time taken for Margsalia and Bray for 100 samples:", MGT1)

print("Time taken for Box miller for 10000 samples:", BMT2)
print("Time taken for Margsalia and Bray for 10000 samples:", MGT2)

print("Portion of samples reject in Margsalia and Bray method for 100 samples:", rejects1)
print("Portion of samples reject in Margsalia and Bray method for 10000 samples:", rejects2)
print("1-pi/4:", (1-cmath.pi/4))