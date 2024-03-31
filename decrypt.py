import os
from calculate_block_size import calculate_block_size
from calculate_start_offsets import calculate_start_offsets

def getInfectedFileFromOriginal(infected_files, original_file):
    for infected_file in infected_files:
        if infected_file.startswith(original_file):
            return infected_file

    return None

infected_files_dir = "infected_files"
original_files_dir = "original_files"

# Get a list of all the infected (encrypted) files
infected_files = [file for file in os.listdir(path=infected_files_dir) if os.path.isfile(file)]

# Iterate over the original files
for file in os.listdir(path=original_files_dir):
    if not os.path.isfile(file):
        continue
    # Get the corresponding infected (encrypted) file
    infected = getInfectedFileFromOriginal(infected_files, file)
    
    # Main algorithm
    nbs = calculate_block_size(infected_files_dir + "/" + file)
    sp1, sp2 = calculate_start_offsets(file)  # stores sp1 and sp2 in hex

    size = os.path.getsize(file)
    iter = size//(0x1000 + nbs)
    offset = 0
