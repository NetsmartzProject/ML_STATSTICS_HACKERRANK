import pandas as pd
import numpy as np
import math

def custom_round(num, decimals=1):
    factor = 10 ** decimals
    temp = math.floor(num * factor + 0.5) / factor
    print(temp,"temp")
    return temp

# Input
# _ = input()  # Discard input as it's not used
i=input()
s=input()
numbers = list(map(int, s.split()))
numbers_series = pd.Series(numbers)
print(numbers_series,"Number Series")

# Calculate statistics
mean = numbers_series.mean()
# Used to calaculete mean of the series . for egample x1+x2+x3+...+xn/n
median = numbers_series.median() 
# Used to calculate median of the series. for example if n is odd then it is (n+1)/2 and if n is even then it is (n/2 + n/2+1)/2
mode = numbers_series.mode()[0]
# Used to calculate mode of the series. It is the number that appears most frequently in the series
std = numbers_series.std(ddof=0) 
# Used to calculate standard deviation of the series. It is the square root of the variance

# Print mean, median, mode, and std
print(f"{custom_round(mean):.1f}")
print(f"{custom_round(median):.1f}")
print(mode)
print(f"{custom_round(std):.1f}")

# Calculate 95% confidence interval
margin_of_error = 1.96 * (std / np.sqrt(len(numbers_series))) 
#These are the z-scores for the most common confidence intervals: 
#`2.576`is the z-score for a 99% confidence interval 
#`2.807`is the z-score for a 99.5% confidence interval
#`3.291`is the z-score for a 99.9% confidence interval
#`2.326` is the z-score for a 98% confidence interval
#`1.96` is the z-score for a 95% confidence interval
#`1.645` is the z-score for a 90% confidence interval
#`1.440`is the z-score for a 85% confidence interval
#`1.282`is the z-score for a 80% confidence interval
#`std / np.sqrt(len(numbers_series))` is the standard error of the mean

lower_bound, upper_bound = mean - margin_of_error, mean + margin_of_error

# Print confidence interval
print(f"{custom_round(lower_bound):.1f} {custom_round(upper_bound):.1f}")
