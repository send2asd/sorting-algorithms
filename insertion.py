import time
import datetime
comp_cnt_insertion_srt = 0
def insertion_sort(A):
    global comp_cnt_insertion_srt
    for j in range(1, len(A)):
 
        key = A[j]
        i = j-1
        while i >=0 and A[i]>key:
                A[i+1] = A[i]
                i = i-1
                comp_cnt_insertion_srt = comp_cnt_insertion_srt+1
        A[i+1] = key
        comp_cnt_insertion_srt = comp_cnt_insertion_srt+1

def run_insertion_sort(array):
    global comp_cnt_insertion_srt
    input_count =len(array)
    start_time_insertion_srt = datetime.datetime.now()
    insertion_sort(array)
    end_time_insertion_srt = datetime.datetime.now()
    ttl_time_insertion_srt = (end_time_insertion_srt - start_time_insertion_srt)
    ttl_time_insertion_srt = (int(ttl_time_insertion_srt.total_seconds()*1000))
    print(input_count,comp_cnt_insertion_srt,ttl_time_insertion_srt)
    print(comp_cnt_insertion_srt)
    values = [input_count,comp_cnt_insertion_srt,ttl_time_insertion_srt]
    f = open("output.txt", "a")
    f.writelines('\nInsertion sort\n')
    f.writelines(",".join(map(str,values)))
    f.writelines('\n')

if __name__ == "__main__":
    flname = input('Enter a filename: ')
    print(flname)
    #sys.setrecursionlimit(1500000000)
    with open(flname, "r") as f:
        y = f.read()
        A = [ int(x) for x in y.split() ] #cast to int

    run_insertion_sort(A)