from collections import Counter
from typing import List
from linear_algebra import sum_of_squares, dot
import math

# num_friends taken from dsfs github
num_friends = [100.0,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,
               13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,
               9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,
               7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,
               6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,
               4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,
               2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
               1,1]

# Simplest statistics, number of friends
num_points = len(num_friends)

# Largest and Smallest Values
largest_value = max(num_friends)
smallest_value = min(num_friends)

# Central Tendencies - we want to know where our data is centered
# Central Tendencies - Mean
def mean(xs: List[float]) -> float: 
    """Given a list of points, find the mean. """
    return sum(xs)/len(xs)


assert round(mean(num_friends), 4) == 7.3333, "Logical Error in mean()"


# Central Tendencies - Median
def __median_odd(xs: List[float]) -> float: 
    """If len(xs) is odd, the median is the middle element"""
    return sorted(xs)[len(xs) // 2]

def __median_even(xs: List[float]) -> float: 
    """If len(xs) is odd, the median is the middle element"""
    # return sorted(xs)[(len(xs) // 2) -1: (len(xs) // 2) +1] / 2
    # Or
    sorted_xs = sorted(xs)
    upper_midpoint = len(xs) // 2
    return (sorted_xs[upper_midpoint-1] + sorted_xs[upper_midpoint]) / 2

def median(v: List[float]) -> float: 
    """Finds the "middle-most" value of v."""
    
    return __median_odd(v) if len(v) % 2 else __median_even(v)
    
    
assert median([1, 10, 2, 9, 5]) == 5, "Logical error in median()"
assert median([1, 9, 2, 10]) == (2 + 9) / 2, "Logical error in median()"


# Central Tendencies - Quartile
# A more generalized version of median is quartile. 
# Median is nothing but 0.5 quartile. 
def quantile(xs: List[float], p: float) -> float: 
    """Returns the pth-percentile value in x"""
    
    p_index = int(len(xs) * p)
    return sorted(xs)[p_index]


one_to_hundred = list(range(100))
assert quantile(one_to_hundred, 0.10) == 10, "Logical Error in quantile()"
assert quantile(one_to_hundred, 0.25) == 25, "Logical Error in quantile()"
assert quantile(one_to_hundred, 0.75) == 75, "Logical Error in quantile()"
assert quantile(one_to_hundred, 0.90) == 90, "Logical Error in quantile()"


# Central Tendencies - Mode
def mode(x: List[float]) -> List[float]: 
    """Returns a list since there might be more than one mode."""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i 
            for x_i, count in counts.items()
            if count == max_count]
    
    
assert set(mode(num_friends)) == {1, 6}, "Logical Error in mode()"


# Dispersion - how spread the data is.
# Dispersion - Range
def data_range(xs: List[float]) -> float: 
    """Gives the difference between maximum and minimum values."""
    return max(xs) - min(xs)


assert data_range(num_friends) == 99, "Logical Error in data_range()"


# Dispersion - Variance
def de_mean(xs: List[float]) -> List[float]: 
    """Translate xs by subtracting its mean (the result would have 0 mean.)
    
       de_mean() stands for deviation mean.
    """
    x_bar = mean(xs)
    return [x - x_bar for x in xs]

def variance(xs: List[float]) -> List[float]:
    """Almost the average squared deviation from the mean"""
    assert len(xs) >=2, "Variance requries at least two elements."
    
    n = len(xs)
    deviation = de_mean(xs)
    return sum_of_squares(deviation) / (n-1)

    
assert 81.54 < variance(num_friends) < 81.55, "Logical Error in variance()"


# Dispersion - Standard deviation - prone to outliers
def standard_deviation(xs: List[float]) -> float: 
    """The standard deviation is the square root of the variance."""
    return math.sqrt(variance(xs))


assert 9.02 < standard_deviation(num_friends) < 9.04, "Logical Error in \
    standard_deviation()"


# Dispersion - Interquartile Range - unaffected by small number of outliers.
def interquartile_range(xs: List[float]) -> float:
    """Returns the difference between the 75%-ile and the 25%-ile."""
    return quantile(xs, 0.75) - quantile(xs, 0.25)


assert interquartile_range(num_friends) == 6, "Logical Error in \
    interquartile_range()"


# Variation between Variables - Covariance
def covariance(xs: List[float], ys: List[float]) -> float:
    """Return the covariance of the two lists xs and ys."""
    assert len(xs) == len(ys), "Lists of different lenght passed!"
    
    n = len(xs)
    x_deviation = de_mean(xs)
    y_deviation = de_mean(ys)
    return dot(x_deviation, y_deviation) / (n-1)
    

# taken from dsfs github
daily_minutes = [1,68.77,51.25,52.08,38.36,44.54,57.13,51.4,41.42,31.22,34.76,
                 54.01,38.79,47.59,49.1,27.66,41.03,36.73,48.65,28.12,46.62,
                 35.57,32.98,35,26.07,23.77,39.73,40.57,31.65,31.21,36.32,
                 20.45,21.93,26.02,27.34,23.49,46.94,30.5,33.8,24.23,21.4,
                 27.94,32.24,40.57,25.07,19.42,22.39,18.42,46.96,23.72,26.41,
                 26.97,36.76,40.32,35.02,29.47,30.2,31,38.11,38.18,36.31,21.03,
                 30.86,36.07,28.66,29.08,37.28,15.28,24.17,22.31,30.17,25.53,
                 19.85,35.37,44.6,17.23,13.47,26.33,35.02,32.09,24.81,19.33,
                 28.77,24.26,31.98,25.73,24.86,16.28,34.51,15.23,39.72,40.8,
                 26.06,35.76,34.76,16.13,44.04,18.03,19.65,32.62,35.59,39.43,
                 14.18,35.24,40.13,41.82,35.45,36.07,43.67,24.61,20.9,21.9,
                 18.79,27.61,27.21,26.61,29.77,20.59,27.53,13.82,33.2,25,33.1,
                 36.65,18.63,14.87,22.2,36.81,25.53,24.62,26.25,18.21,28.08,
                 19.42,29.79,32.8,35.99,28.32,27.79,35.88,29.06,36.28,14.1,
                 36.63,37.49,26.9,18.58,38.48,24.48,18.95,33.55,14.24,29.04,
                 32.51,25.63,22.22,19,32.73,15.16,13.9,27.2,32.01,29.27,33,
                 13.74,20.42,27.32,18.23,35.35,28.48,9.08,24.62,20.12,35.26,
                 19.92,31.02,16.49,12.16,30.7,31.22,34.65,13.13,27.51,33.2,
                 31.57,14.1,33.42,17.44,10.12,24.42,9.82,23.39,30.93,15.03,
                 21.67,31.09,33.29,22.61,26.89,23.48,8.38,27.81,32.35,23.84]

daily_hours = [dm / 60 for dm in daily_minutes]

assert 22.42 < covariance(num_friends, daily_minutes) < 22.43, "Logical error \
    in covariance()"
assert 22.42 / 60 < covariance(num_friends, daily_hours) < 22.43 / 60, "Logica\
    l error in covariance()"


# Variation between Variables - Correlation
def correlation(xs: List[float], ys: List[float]) -> float: 
    """Measures how much xs and ys vary in tandem about their means."""
    assert len(xs) == len(ys), "Lists of different lenght passed!"
    
    stdev_x = standard_deviation(xs)
    stdev_y = standard_deviation(ys)
    if stdev_x > 0 and stdev_y > 0: 
        return covariance(xs, ys)/(stdev_x * stdev_y)
    else: 
        return 0
    
    
assert 0.24 < correlation(num_friends, daily_minutes) < 0.25, "Logical error \
    in correlation()"
assert 0.24 < correlation(num_friends, daily_hours) < 0.25, "Logical error \
    in correlation()"