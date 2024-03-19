import sys
import os

file = sys.argv[1]

print("Calculating data block size of file: " + file + "...")

file_size = os.path.getsize(file)
nbs = 0

if file_size <= 0x1000:
    print(nbs)
    exit()
elif file_size < 0x20000:
    r = file_size >> 12
elif file_size < 0x100000:
    r = ((file_size >> 12)*30)//100
elif file_size < 0xA00000:
    r = ((file_size >> 12)*20)//100
elif file_size < 0x6400000:
    r = ((file_size >> 12)*10)//100
elif file_size < 0x40000000:
    r = ((file_size >> 12)*5)//100
else:
    r = ((file_size >> 12)*1)//100

if r == 1:
    print(nbs)
    exit()

nbs = (file_size - (r << 12))//(r - 1)

print(nbs)
