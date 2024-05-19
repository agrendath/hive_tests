import os
from calculate_block_size import calculate_block_size
from calculate_start_offsets import calculate_start_offsets
import random 
import copy
from os.path import isfile, join

def getInfectedFileFromOriginal(infected_files, original_file):
    for infected_file in infected_files:
        infected = infected_file.split("/")[-2] + infected_file.split("/")[-1]
        original = original_file.split("/")[-2] + original_file.split("/")[-1]
        if infected.startswith(original):
            return infected_file
    raise "Error_No_Existing_File"

infected_files_dir = "infected_files/"
original_files_dir = "original_files/"

# Get a list of all the infected (encrypted) files
subdirs = ["21000/"]#, "150000/", "501000/", "1000000/", "5000000/", "10000000/", "1000000000/"]
infected_files = []
original_files = []

# Add files from all the subdirectories
for subdir in subdirs:
    infected_files += [(subdir + file) for file in os.listdir(path=infected_files_dir + subdir) if isfile(join(infected_files_dir + subdir, file))]
    original_files += [(subdir + file) for file in os.listdir(path=original_files_dir + subdir) if isfile(join(original_files_dir + subdir, file))]

print("Starting decryption process...")
EQS = list()
# Iterate 
# over the original files
stop = 500
for original_file in original_files :
    stop -= 1
    # Get the corresponding infected (encrypted) file
    infected_file = getInfectedFileFromOriginal(infected_files, original_file)
    print("File: " + original_file + " -> " + infected_file + "...")

    if_content = open(infected_files_dir + infected_file, "rb").read()
    of_content = open(original_files_dir + original_file, "rb").read()
    
    # First we run the first algorithm on the full file path
    nbs = calculate_block_size(infected_files_dir + infected_file) ## USING ALGO 1
    size = os.path.getsize(infected_files_dir + infected_file)  # Get the size of the file
    print("Size: " + str(size))

    # Now we remove the path from the file names so that we can perform operations on the pure file names
    infected_file = infected_file.split("/")[-1]
    original_file = original_file.split("/")[-1]
    
    # Now we calculate the start offsets from the file name 
    SP1, SP2 = calculate_start_offsets(infected_file)  # stores sp1 and sp2 in hex ##USING ALGO 2
    # Main algorithm
    iter = size//(0x1000 + nbs)
    print("Will run for " + str(iter) + " iterations (size//0x1000 + nbs) = (size//0x1000 + " + str(nbs) + ")")
    offset = 0
    for i in range (iter + 1):
        print("Iteration " + str(i) + "/" + str(iter) + "...")
        if i == iter :
            ## From paper:
            ## If the last block size is more than 0x1000 bytes, 0x1000 bytes of the last block
            ## starting from the end of the file are encrypted. Otherwise the entire block is encrypted
            if size - 0x1000 > offset:
                offset = size - offset - 0x1000            
        for j in range(0xFFF + 1):
            O1 = offset%0x100000
            O2 = offset%0x400
            if offset > len(if_content) - 1 or offset > len(of_content) - 1:
                print("[!] END OF FILE REACHED")
                break
            tmp = (SP1 + O1, SP2 + O2, if_content[offset] ^ of_content[offset])
            if not tmp in EQS:
                EQS.append(tmp)
            offset += 1
        offset += nbs
    if stop == 0:
        break

EK = [None] * 0xA00000
E = copy.deepcopy(list(EQS)[random.randint(0, len(EQS) - 1)])
EK[E[0]] = random.randint(0, 255)
EQS = list(EQS)

sentinelle = len(EQS) + 1
result = None

print("EQS LENGTH BEFORE SOLVE:", len(EQS))
eqs_popped = 0
for EQ in EQS:
        if ((EK[EQ[0]]) == None)  and ((EK[EQ[1]]) == None):
            continue
        elif ((EK[EQ[0]]) != None)  and ((EK[EQ[1]]) == None):
            EK[EQ[1]] = EK[EQ[0]] ^ int(EQ[2])     
        elif ((EK[EQ[0]]) == None)  and ((EK[EQ[1]]) != None):
            EK[EQ[0]] = EK[EQ[1]] ^ int(EQ[2]) 
        elif ((EK[EQ[0]]) != None) and ((EK[EQ[1]]) != None):
            result = EQ
            EQS.pop(EQS.index(EQ))
            eqs_popped += 1

while not (len(EQS) == sentinelle):
    sentinelle = len(EQS)
    for EQ in EQS:
        if ((EK[EQ[0]]) == None)  and ((EK[EQ[1]]) == None):
            continue
        elif ((EK[EQ[0]]) != None)  and ((EK[EQ[1]]) == None):
            EK[EQ[1]] = EK[EQ[0]] ^ int(EQ[2])     
        elif ((EK[EQ[0]]) == None)  and ((EK[EQ[1]]) != None):
            EK[EQ[0]] = EK[EQ[1]] ^ int(EQ[2]) 
        elif ((EK[EQ[0]]) != None) and ((EK[EQ[1]]) != None):
            result = EQ
            EQS.pop(EQS.index(EQ))
            eqs_popped += 1
            if eqs_popped % 100 == 0:
                print("Number element poped = ",eqs_popped)

print("EQS Length:", len(EQS))
print("Amount of EQ popped:", eqs_popped)
print("Last popped EQ:", result)

# Calculate which percentage of EK we acquired
EK_percentage = 0
for i in range(len(EK)):
    if EK[i] != None:
        EK_percentage += 1
EK_percentage = (EK_percentage/len(EK)) * 100
print("Percentage of EK acquired:", EK_percentage,"%")

# Write EK to a file called EK.txt, but only the spaces that are not None
print("Writing EK to file...")
with open("EK.txt", "w") as f:
    for i in range(len(EK)):
        if EK[i] != None:
            f.write(str(i) + ": " + str(EK[i]) + "\n")

# Write EQS to a file
print("Writing EQS to file...")
with open("EQS.txt", "w") as f:
    for i in range(len(EQS)):
        f.write(str(EQS[i]) + "\n")

