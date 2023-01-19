import time
import datetime
comp_cnt_merge_3_way_srt = 0
def merge_3_way(array, start, mid1, mid2, end):
    global comp_cnt_merge_3_way_srt
    left_array = array[start -1 : mid1]
    mid_array = array[mid1: mid2 + 1]
    right_array = array[mid2 + 1 : end]

    left_array.append(float('inf'))
    mid_array.append(float('inf'))
    right_array.append(float('inf'))
    
    ind_left = 0
    ind_mid = 0
    ind_right = 0
    for i in range(start-1, end):
        comp_cnt_merge_3_way_srt = comp_cnt_merge_3_way_srt+1
        minimum = min([left_array[ind_left], mid_array[ind_mid], right_array[ind_right]])
        if minimum == left_array[ind_left]:
            array[i] = left_array[ind_left]
            ind_left += 1
        elif minimum == mid_array[ind_mid]:
            comp_cnt_merge_3_way_srt = comp_cnt_merge_3_way_srt+1
            array[i] = mid_array[ind_mid]
            ind_mid += 1
        else:
            comp_cnt_merge_3_way_srt = comp_cnt_merge_3_way_srt+1
            array[i] = right_array[ind_right]
            ind_right += 1
            
def merge_3_way_sort(array, start, end):

    if len(array[start -1: end]) < 2:
        return array
    else: 
        mid1 = start + ((end - start) // 3)
        mid2 = start + 2 * ((end-start) // 3)

        merge_3_way_sort(array, start, mid1)
        merge_3_way_sort(array, mid1+1, mid2 + 1)
        merge_3_way_sort(array, mid2+2, end)
        merge_3_way(array, start, mid1, mid2, end)
        return array

def run_merge_3_way_sort(array):
    global comp_cnt_merge_3_way_srt
    start_time_merge_3_way_srt = datetime.datetime.now()
    input_count =len(array) #Total number of items
    start = 1 #Start is 1
    end = len(array) #Length of array
    array = merge_3_way_sort(array, start, end)
    end_time_merge_3_way_srt = datetime.datetime.now()
    ttl_time_merge_3_way_srt = (end_time_merge_3_way_srt - start_time_merge_3_way_srt)
    ttl_time_merge_3_way_srt = (int(ttl_time_merge_3_way_srt.total_seconds()*1000))
    print(input_count,comp_cnt_merge_3_way_srt,ttl_time_merge_3_way_srt)
    print(comp_cnt_merge_3_way_srt)
    values = [input_count,comp_cnt_merge_3_way_srt,ttl_time_merge_3_way_srt]
    f = open("output.txt", "a")
    f.writelines('\n3-way Merge sort\n')
    f.writelines(",".join(map(str,values)))
    f.writelines('\n')

if __name__ == "__main__":
    flname = input('Enter a filename: ')
    print(flname)
    #sys.setrecursionlimit(1500000000)
    with open(flname, "r") as f:
        y = f.read()
        A = [ int(x) for x in y.split() ] #cast to int

    input_count =len(A)
    run_merge_3_way_sort(A)