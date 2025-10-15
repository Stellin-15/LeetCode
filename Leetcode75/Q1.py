import numpy as np
from scipy import stats

# Given data
mu_0 = 50      # hypothesized mean
sigma = 2      # population std deviation
x_bar = 51.3   # sample mean
n = 25
alpha = 0.05

# z-statistic
z_stat = (x_bar - mu_0) / (sigma / np.sqrt(n))

# two-tailed p-value
p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))

# critical z for two-tailed test
z_crit = stats.norm.ppf(1 - alpha/2)

print(f"z-statistic: {z_stat:.4f}")
print(f"Critical z-value (±): {z_crit:.4f}")
print(f"p-value: {p_value:.4f}")

if abs(z_stat) > z_crit:
    print("Reject H₀ → The mean burning rate significantly differs from 50 cm/s.")
else:
    print("Fail to reject H₀ → No significant difference from 50 cm/s.")

