"""
------------------------------------------------------------------------
CP164 Lab 10, Task 03
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-03-22"
------------------------------------------------------------------------
"""
from test_Sorts_array import SORTS, test_sort

print(
    f"n:   100       |      Comparisons       | |         Swaps          |")
print("Algorithm      In Order Reversed   Random In Order Reversed   Random")
print("-------------- -------- -------- -------- -------- -------- --------")

for values in SORTS:
    test_sort(values[0], values[1])
