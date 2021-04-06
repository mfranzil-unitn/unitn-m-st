import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
we consider a list of integers going from 2^0 to 2^159, and we use sys.getsizeof to inspect how many bytes are actually used to store the integer
"""
import sys
int_sizes = {}
for i in range(160):
    int_sizes[i] = sys.getsizeof(2 ** i)
int_sizes = pd.Series(int_sizes)

#Plotting the results
plt.figure()
ax = int_sizes.plot(ylim=[0, 60])
ax.set_ylabel('number of bytes')
ax.set_xlabel('integer (log scale)')
ax.set_title('number of bytes used to store an integer (python 3.6)')
ax.set_xticks(range(0, 160, 10))
labels = ['$2^{%d}$' % x for x in range(0, 160, 10)]
ax.set_xticklabels(labels)
ax.tick_params(axis='x', labelsize=18)
ax.tick_params(axis='y', labelsize=12)
plt.show()

print(int_sizes[29:31].head())

# Overflows in Numpy
print('='*80)
print('Overflows in Numpy')
a = np.array([2**63 - 1, 2**63 - 1], dtype=int)
print(a)
print(a.dtype)

print('Adding 1 to array will cause a silent overflow')
print(a+1)

print('Similarly, sum() function will result in overflow')
print(a.sum())

print('However, mean function works correctly, as the values are casted to float')
print(a.mean())

if __name__ == '__main__':
    print('a')
