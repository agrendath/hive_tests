import os
from calculate_block_size import calculate_block_size
from calculate_start_offsets import calculate_start_offsets
import random 
import copy

def getInfectedFileFromOriginal(infected_files, original_file):
    for infected_file in infected_files:
        if infected_file.startswith(original_file):
            return infected_file
    raise "Error_No_Existing_File"

infected_files_dir = "infected_files"
original_files_dir = "original_files"

# Get a list of all the infected (encrypted) files
infected_files = [file for file in os.listdir(path=infected_files_dir) if os.path.isfile(file)]
original_files = [file for file in os.listdir(path=original_files_dir) if os.path.isfile(file)]

# Iterate over the original files
for original_file in original_files :
    # Get the corresponding infected (encrypted) file
    infected_file = getInfectedFileFromOriginal(infected_files, original_file)
    
    # Main algorithm
    nbs = calculate_block_size(infected_files_dir + "/" + infected_file) ## USING ALGO 1
    SP1, SP2 = calculate_start_offsets(infected_file)  # stores sp1 and sp2 in hex ##USING ALGO 2

    size = os.path.getsize(infected_file)
    iter = size//(0x1000 + nbs)
    offset = 0
    EQS = {}
    for i in range (iter+1):
        if i == iter :
            offset = ...
        for j in range(0xFFF +1):
            O1 = offset%0x100000
            O2 = offset%0x1000
            EQS.add((SP1 + O1, SP2 + O2, infected_file[offset] ^ original_file[offset]))
            offset += 1
        offset += nbs

EK = [0xA00000 for _ in range(len(EQS))]
E = copy.deepcopy(list(EQS)[random.randint(0, len(EQS-1))])
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