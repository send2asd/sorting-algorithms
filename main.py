import sys
import time
import datetime
import merge
import insertion
import heap
import merge_3_way





def main(array):
    
    # Merge sort
    merge.run_merge_sort(array)

    # Insertion sort
    insertion.run_insertion_sort(array)

    # Heap sort
    heap.run_heap_sort(array)

     # 3-way Merge sort
    merge_3_way.run_merge_3_way_sort(array)


if __name__ == "__main__":
    flname = input('Enter a filename: ')
    print(flname)
    #sys.setrecursionlimit(1500000000)
    with open(flname, "r") as f:
        y = f.read()
        A = [ int(x) for x in y.split() ] #cast to int

    main(A)

