import random, time
import tabulate
import sys
sys.setrecursionlimit(150000)
def ssort(L):
    ### selection sort
    if (len(L) == 1):
        return(L)
    else:
        m = L.index(min(L))
        L[0], L[m] = L[m], L[0]
        return [L[0]] + ssort(L[1:])

def qsort(a, pivot_fn):
    if len(a) <= 1:
        return a
        # create pibot
    pivot_index = pivot_fn(a)
    pivot = a[pivot_index]

    # make list into 3 parts left right and equal
    left = [x for x in a if x < pivot]
    e = [x for x in a if x == pivot]
    r = [x for x in a if x > pivot]

    # Recursively sort sublists and combine
    return qsort(left, pivot_fn) + e + qsort(r, pivot_fn)


def time_search(sort_fn, mylist):
    """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds.
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000
    ###

def compare_sort(sizes=[20, 40, 100, 200, 400, 1000, 2000, 4000, 10000, 20000]):
    """
    Compare the running time of different sorting algorithms.

    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """
    ### TODO - sorting algorithms for comparison
    qsort_fixed_pivot = lambda a: qsort(a, lambda x: 0)  #Automatically pick first element
    qsort_random_pivot = lambda a: qsort(a, lambda x: random.randrange(len(x)))
    tim_sort = lambda a: sorted(a)
    result = []
    for size in sizes:
        # create list in ascending order
        mylist = list(range(size))
        # shuffles list if needed
        random.shuffle(mylist)
        result.append([
            len(mylist),
            time_search(qsort_fixed_pivot, mylist),
            time_search(qsort_random_pivot, mylist),
            time_search(ssort, mylist),
            time_search(tim_sort, mylist),
        ])
    return result
    ###

def print_results(results):
    """ change as needed for comparisons """
    print(tabulate.tabulate(results,
                            headers=['n', 'qsort-fixed-pivot', 'qsort-random-pivot', 'ssort', 'timsort'],
                            floatfmt=".3f",
                            tablefmt="github"))

def test_print():
    print_results(compare_sort())

random.seed()
test_print()
print("hell")