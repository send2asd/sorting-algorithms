import time
import datetime
comp_cnt_merge_srt = 0
def merge(sub_array_1, sub_array_2):
    global comp_cnt_merge_srt
    i, j = 0, 0
    result = []
    while i < len(sub_array_1) and j < len(sub_array_2):
        comp_cnt_merge_srt = comp_cnt_merge_srt+1
        if sub_array_1[i] < sub_array_2[j]:
            result.append(sub_array_1[i])
            i += 1
        else:
            result.append(sub_array_2[j])
            j += 1

    result += sub_array_1[i:]
    result += sub_array_2[j:]
    return result

def merge_sort(array):
    if len(array) <= 1:  
        return array

    # divide array in two part
    half = len(array) // 2
    sub_array_1 = merge_sort(array[:half])
    sub_array_2 = merge_sort(array[half:])

    return merge(sub_array_1, sub_array_2)


def run_merge_sort(array):
    global comp_cnt_merge_srt
    input_count =len(array)
    start_time_merge_srt = datetime.datetime.now()
    merge_sort(array)
    end_time_merge_srt = datetime.datetime.now()
    ttl_time_merge_srt = (end_time_merge_srt - start_time_merge_srt)
    ttl_time_merge_srt = (int(ttl_time_merge_srt.total_seconds()*1000))
    print(input_count,comp_cnt_merge_srt,ttl_time_merge_srt)
    print(comp_cnt_merge_srt)
    values = [input_count,comp_cnt_merge_srt,ttl_time_merge_srt]
    f = open("output.txt", "a")
    f.writelines('\nMerge sort\n')
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
    run_merge_sort(A)
