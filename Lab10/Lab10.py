import numpy as np
import matplotlib.pyplot as plt

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def bGen(n, b):
    res = list()
    while(n>0):
        res.append(n%b)
        n=int(n/b)
    return res

def vanDerCorput(n, b):
    res = list()
    for i in range(1, n+1):
        tempRes = 0
        di = bGen(i, b)
        poww = 0
        for d in di:
            tempRes+=d/(pow(b, poww+1))
            poww+=1
        res.append(tempRes)
    return res

# Q1 (a)

print(color.BOLD + color.UNDERLINE + color.RED + "Q1" + color.END)

v1 = vanDerCorput(25, 2)
print(color.BOLD + color.GREEN + f"First 25 values of Van Der Corput Sequence:\n" + color.END + color.YELLOW + f"{v1}" + color.END)


# Q1 (b)

v2 = vanDerCorput(1000, 2)
v2_x = v2[:-1]
v2_y = v2[1:]
plt.figure(figsize = (5.5,5))
plt.scatter(v2_x, v2_y, s=5, c='r')
plt.title(f"Scatter plot of the generated sequence using Van Der Corput for x=1000 and b=2")
plt.show()



# Q2

def uGen(a,b,m,N,seed):
    x = seed
    u = x/m
    res = []
    for _ in range(17):
        x = (a*x + b)%m
        u = x/m
        res.append(u)
    for i in range(17, N):
        u = res[i-17]-res[i-5]
        if(u<0): u+=1
        res.append(u)
    return res

cases = [100, 100000]

for case in cases:
    vand = vanDerCorput(case, 2)
    lcg = uGen(1597, 25, 244944, case, 8)
    binn = 100
    if(case==100):
        binn = 20
    
    plt.figure(figsize = (10,5))
    
    plt.subplot(1, 2, 1)    
    plt.hist(vand, bins=binn, color = 'g')
    plt.title("Van Der Corput sequence")
    
    plt.subplot(1,2,2)
    plt.hist(lcg, bins=binn, color='r')
    plt.title("LCG \n a=1597, b=25, m=244944, seed=8")
    plt.tight_layout()
    plt.suptitle(f"For {case} samples")
    plt.show()


# Q3)

for case in cases:
    x_i = vanDerCorput(case, 2)
    y_i = vanDerCorput(case, 3)
    
    plt.scatter(x_i, y_i)
    plt.title(f"Halton Sequence for {case} samples")
    plt.show()





