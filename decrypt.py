import os
from calculate_block_size import calculate_block_size
from calculate_start_offsets import calculate_start_offsets
import random 
import copy
from os.path import isfile, join

def getInfectedFileFromOriginal(infected_files, original_file):
    for infected_file in infected_files:
        if infected_file.startswith(original_file):
            return infected_file
    raise "Error_No_Existing_File"

infected_files_dir = "infected_files/"
original_files_dir = "original_files/"

# Get a list of all the infected (encrypted) files
infected_files = [file for file in os.listdir(path=infected_files_dir) if isfile(join(infected_files_dir, file))]
original_files = [file for file in os.listdir(path=original_files_dir) if isfile(join(original_files_dir, file))]

print("Starting decryption process...")

EQS = {}
# Iterate over the original files
for original_file in original_files :
    # Get the corresponding infected (encrypted) file
    infected_file = getInfectedFileFromOriginal(infected_files, original_file)
    print("File: " + original_file + " -> " + infected_file + "...")
    
    # Main algorithm
    nbs = calculate_block_size(infected_files_dir + "/" + infected_file) ## USING ALGO 1
    SP1, SP2 = calculate_start_offsets(infected_file)  # stores sp1 and sp2 in hex ##USING ALGO 2

    size = os.path.getsize(infected_file)
    iter = size//(0x1000 + nbs)
    offset = 0
    EQS = {}
    for i in range (iter+1):
        if i == iter :
            ## From paper:
            ## If the last block size is more than 0x1000 bytes, 0x1000 bytes of the last block
            ## starting from the end of the file are encrypted. Otherwise the entire block is encrypted
            if size - 0x1000 > offset:
                offset += size - offset - 0x1000
        for j in range(0xFFF +1):
            O1 = offset%0x100000
            O2 = offset%0x1000
            EQS.add((SP1 + O1, SP2 + O2, infected_file[offset] ^ original_file[offset]))
            offset += 1
        offset += nbs

if EQS == {}:
    print("No EQS found")
    exit()

EK = [None] * 0xA00000
E = copy.deepcopy(list(EQS)[random.randint(0, len(EQS) - 1)])
EK[E[0]] = random.randint(0, 255)
EQS = tuple(EQS)

sentinelle = len(EQS)

while len(EQS) == sentinelle:
    for EQ in EQS:
        if ((EK[EQ[0]]) == None)  and ((EK[EQ[1]]) == None):
            continue
        elif ((EK[EQ[0]]) != None)  and ((EK[EQ[1]]) == None):
            EK[EQ[1]] = EK[EQ[0]] ^ EK[EQ[2]]      
        elif ((EK[EQ[0]]) == None)  and ((EK[EQ[1]]) != None):
            EK[EQ[0]] = EK[EQ[1]] ^ EK[EQ[2]]      
        elif ((EK[EQ[0]]) != None) and ((EK[EQ[1]]) != None):
            EQS.pop(EQ)

print(EQS)