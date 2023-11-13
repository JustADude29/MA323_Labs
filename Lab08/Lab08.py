import numpy as np
from scipy.stats import poisson, weibull_min

# Parameters
lambda_val = 2.9  # Lambda for Poisson distribution
k = 0.8  # Shape parameter for Weibull distribution
sigma = 3  # Scale parameter for Weibull distribution
total_rainfall_threshold = 5  # Threshold for emergency water allocation

# Monte Carlo Method
def monte_carlo_simulation(num_trials):
    count_below_threshold = 0

    for _ in range(num_trials):
        # Step 1: Simulate the number of rainfall events
        S = poisson.rvs(lambda_val)

        # Step 2: Simulate rainfall depths for each event
        rainfall_depths = weibull_min.rvs(k, scale=sigma, size=S)

        # Step 3: Calculate total rainfall
        total_rainfall = np.sum(rainfall_depths)

        # Step 4: Check if total rainfall is below the threshold
        if total_rainfall < total_rainfall_threshold:
            count_below_threshold += 1

    probability = count_below_threshold / num_trials
    return probability

# Stratification Method
def stratification_simulation(num_trials):
    strata = [0, 1, 2, 3, 4, 5, 6]  # Strata based on S values
    probabilities = []

    for S in strata:
        # Step 1: Calculate the probability of S for this stratum
        stratum_probability = poisson.pmf(S, lambda_val)

        # Step 2: Perform Monte Carlo simulation for this stratum
        count_below_threshold = 0

        for _ in range(num_trials):
            # Simulate rainfall depths for this stratum
            rainfall_depths = weibull_min.rvs(k, scale=sigma, size=S)

            # Calculate total rainfall for this stratum
            total_rainfall = np.sum(rainfall_depths)

            # Check if total rainfall is below the threshold
            if total_rainfall < total_rainfall_threshold:
                count_below_threshold += 1

        stratum_probability *= count_below_threshold / num_trials
        probabilities.append(stratum_probability)

    overall_probability = sum(probabilities)
    return overall_probability

# Number of trials for Monte Carlo method
num_trials_monte_carlo_100 = 100
num_trials_monte_carlo_10000 = 10000

# Number of trials for stratification method
num_trials_stratification_100 = 100
num_trials_stratification_10000 = 10000

# Monte Carlo method
monte_carlo_prob_100 = monte_carlo_simulation(num_trials_monte_carlo_100)
monte_carlo_prob_10000 = monte_carlo_simulation(num_trials_monte_carlo_10000)

# Stratification method
stratification_prob_100 = stratification_simulation(num_trials_stratification_100)
stratification_prob_10000 = stratification_simulation(num_trials_stratification_10000)

print("Monte Carlo Method:")
print("Probability (n=100):", monte_carlo_prob_100)
print("Probability (n=10000):", monte_carlo_prob_10000)

print("\nStratification Method:")
print("Probability (n=100):", stratification_prob_100)
print("Probability (n=10000):", stratification_prob_10000)
