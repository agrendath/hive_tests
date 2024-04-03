import sys
import os

#file = sys.argv[1]

#print("Calculating data block size of file: " + file + "...")

def calculate_block_size(file_path):
    file_size = os.path.getsize(file_path)
    nbs = 0

    if file_size <= 0x1000:
        return nbs
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
        return nbs

    nbs = (file_size - (r << 12))//(r - 1)

    return nbs

# calculate block size for the file decrypt.py
tmp = calculate_block_size("C:\\Users\\antho\\Downloads\\ova-20240401T121536Z-001.zip")
print(tmp)
