nsity=False)
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