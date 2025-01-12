
from collections import Counter
import matplotlib.pyplot as plt

# num_friends taken from dsfs github
num_friends = [100.0,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

friends_count = Counter(num_friends)



xs = range(101)
ys = [friends_count[x] for x in xs]

plt.bar(xs, ys)
plt.axis([0, 101, 0, 10])
plt.title("Histogram of Friends Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()


num_points = len(num_friends)


largest_value = max(num_friends)
smallest_value = min(num_friends)


from typing import List
def mean(xs: List[float]) -> float: 
    return sum(xs)/len(xs)

mean(num_friends)


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


def quantile(xs: List[float], p: float) -> float: 
    """Returns the pth-percentile value in x"""
    
    p_index = int(len(xs) * p)
    return sorted(xs)[p_index]


one_to_hundred = list(range(100))
assert quantile(one_to_hundred, 0.10) == 10, "Logical Error in quantile()"
assert quantile(one_to_hundred, 0.25) == 25, "Logical Error in quantile()"
assert quantile(one_to_hundred, 0.75) == 75, "Logical Error in quantile()"
assert quantile(one_to_hundred, 0.90) == 90, "Logical Error in quantile()"


def mode(x: List[float]) -> List[float]: 
    """Returns a list since there might be more than one mode."""
    
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i 
            for x_i, count in counts.items()
            if count == max_count]
    
one_to_hundred = list(range(100))
one_to_hundred.extend([10]*3)
assert mode(one_to_hundred) == [10], "Logical Error in mode()"


def data_range(xs: List[float]) -> float: 
    return max(xs) - min(xs)

assert data_range(one_to_hundred) == 100, "Logical Error in data_range()"





