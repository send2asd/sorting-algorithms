import time
import datetime
comp_cnt_heap_srt = 0

def heapify(array, n, i):
    count=0
    largest = i  
    l = 2 * i + 1     
    r = 2 * i + 2     
    if l < n and array[i] < array[l]:
        largest = l
    if r < n and array[largest] < array[r]:
        largest = r
    if largest != i:
        count += 1
        array[i],array[largest] = array[largest],array[i]
        count += heapify(array, n, largest)
    return count

def heap_sort(array):
    n = len(array)
    global comp_cnt_heap_srt
    for i in range(n, -1, -1):
        heapify(array, n, i)  
        comp_cnt_heap_srt += heapify(array, i, 0)
    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i] 
        comp_cnt_heap_srt += heapify(array, i, 0)
    return comp_cnt_heap_srt


def run_heap_sort(array):
    global comp_cnt_heap_srt
    input_count =len(array)
    start_time_heap_srt = datetime.datetime.now()
    heap_sort(array)
    end_time_heap_srt = datetime.datetime.now()
    ttl_time_heap_srt = (end_time_heap_srt - start_time_heap_srt)
    ttl_time_heap_srt = (int(ttl_time_heap_srt.total_seconds()*1000))
    print(input_count,comp_cnt_heap_srt,ttl_time_heap_srt)
    print(comp_cnt_heap_srt)
    values = [input_count,comp_cnt_heap_srt,ttl_time_heap_srt]
    f = open("output.txt", "a")
    f.writelines('\nHeap sort\n')
    f.writelines(",".join(map(str,values)))
    f.writelines('\n')


if __name__ == "__main__":
    flname = input('Enter a filename: ')
    print(flname)
    #sys.setrecursionlimit(1500000000)
    with open(flname, "r") as f:
        y = f.read()
        A = [ int(x) for x in y.split() ] #cast to int

    run_heap_sort(A)