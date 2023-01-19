import sys
import time
import datetime
from insertion import insertion


comparasioncount = 0
flname = input('Enter a filename: ')
#sys.getrecursionlimit())
print(flname)
sys.setrecursionlimit(15000000)
#print ('Number of arguments:', sys.argv, 'arguments.')
#flname = sys.argv[1]

with open(flname, "r") as f:
    y = f.read()
    A = [ int(x) for x in y.split() ] #cast to int

input_count =len(A)

cnt_rr =[]
start_time = datetime.datetime.now()


def main(array):
    return insertion(array)



if __name__ == "__main__":
    main(A)
end_time = datetime.datetime.now()
ttl_time = (end_time - start_time)
ttl_time = round(ttl_time.microseconds/1000,4)
print(input_count,comparasioncount,ttl_time)
print(comparasioncount)
values = [input_count,comparasioncount,ttl_time]
f = open("output.txt", "a")
f.writelines(",".join(map(str,values)))
f.writelines('\n')
f.close()

