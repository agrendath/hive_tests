import os
from calculate_block_size import calculate_block_size
from calculate_start_offsets import calculate_start_offsets

infected_files_dir = "infected_files"
original_files_dir = "original_files"

for file in os.listdir(path=original_files_dir):
    if not os.path.isfile(file):
        continue

    # further code here