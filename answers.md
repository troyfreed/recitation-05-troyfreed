# CMPS 2200 Reciation 5
## Answers

**Name:**Troy Freed and Mike Baron


Place all written answers from `recitation-05.md` here for easier grading.







- **1b.**
Sorted:

      n |   qsort-fixed-pivot |   qsort-random-pivot |    ssort |   timsort |
|-------|---------------------|----------------------|----------|-----------|
|    20 |               0.047 |                0.030 |    0.015 |     0.001 |
|    40 |               0.110 |                0.057 |    0.033 |     0.001 |
|   100 |               0.628 |                0.151 |    0.136 |     0.001 |
|   200 |               2.132 |                0.342 |    0.446 |     0.003 |
|   400 |               7.801 |                0.778 |    2.040 |     0.004 |
|  1000 |              42.507 |                1.860 |   10.846 |     0.009 |
|  2000 |             175.338 |                3.760 |   43.288 |     0.016 |
|  4000 |             685.280 |                7.781 |  196.078 |     0.026 |
| 10000 |            4599.854 |               21.758 | 1408.764 |     0.068 |
| 20000 |           20702.004 |               45.268 | 6063.680 |     0.168 |

Unsorted:

     n |   qsort-fixed-pivot |   qsort-random-pivot |     ssort |   timsort |
|------|---------------------|----------------------|-----------|-----------|
|    20 |               0.034 |                0.042 |     0.016 |     0.001 |
|    40 |               0.056 |                0.060 |     0.036 |     0.002 |
|   100 |               0.128 |                0.160 |     0.236 |     0.006 |
|   200 |               0.272 |                0.342 |     0.549 |     0.013 |
|   400 |               0.642 |                0.764 |     2.485 |     0.029 |
|  1000 |               2.026 |                2.313 |    13.701 |     0.075 |
|  2000 |               3.827 |                4.332 |    82.166 |     0.165 |
|  4000 |               8.362 |                9.302 |   242.589 |     0.353 |
| 10000 |              25.555 |               25.961 |  1677.372 |     0.963 |
| 20000 |              45.360 |               54.349 | 10136.747 |     2.116 |


Quicksort (random pivot): In both cases of whether the list was shuffled or not
it ran in O(nlogn) complexity, which aligns with the average case performance of quicksort.

Quicksort (set pivot): In the case of a sorted list it ran in O(n^2) complexity because 
it always took the first element which is the worst case scenario. In an unsorted list
the first element is effectively a random element, making it run in the average
case scenario of O(nlogn)

Selection sort: this had a runtime of O(n^2), which was constant for both sorted and unsorted lists,
this can be seen in the table above.

Overall quicksort with a random pivot is the most effective algorithm.

- **1c.**

timsort is much faster in a sorted or unsorted case, in a situation where it is sorted
the second closest is qsort with a random pivot. Even then the runtime for timsort with
a list of 20000 has the same time as a qsort random pivot with a size of 100. 
When it is an unsorted list it slows down, but still is much faster than the fixed
pivot, which is the second fastest.