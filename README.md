# [INFO-F514] - Protocols, cryptanalysis and mathematical cryptology 

Original article : "A Method for Decrypting Data Infected with Hive
Ransomware " (https://arxiv.org/pdf/2202.08477.pdf)




## How to run
Sample of the files used for our experiment can be found at the following Google drive : https://drive.google.com/drive/folders/1xXCEproQ8LHYVu6pQKIwis19RFkQjNnK?usp=sharing

The first step is to create (or download with from our Google Drive link), original files that are not infected. To do that you can run the code. 

```bash
python3 file_creator.py
```

The second step is to infect those files (or using our files that you can find on our Google Drive). 

(All instructions to create the files encrypted by hive and extract them are inside the report)

Once you have all the files (infected and original) :

1) Put all original files inside a folder which has the name ```original_files```in the root of the folder.

2) Put all infected files inside a folder which has the name ```infected_files```in the root of the folder.

After all this step, you must have the following folder structure.
```bash
.
└── HIVE
    ├── calculate_block_size.py
    ├── calculate_startoffsets.py
    ├── decrypt.py
    ├── file_creator.py
    ├── infected_files
    │   ├── 21000
    │   │   ├── file 1
    │   │   └── ...
    │   ├── 150000
    │   │   ├── file 1
    │   │   └── ...
    │   ├── 501000
    │   │   ├── file 1
    │   │   └── ...
    │   ├── 1000000
    │   │   ├── file 1
    │   │   └── ...
    │   ├── 5000000
    │   │   ├── file 1
    │   │   └── ...    
    │   ├── 10000000
    │   │   ├── file 1
    │   │   └── ...
    │   └── 10000000000
    │       ├── file 1
    │       └── ...
    └── original_files
        ├── 21000
        │   ├── file 1
        │   └── ...
        ├── 150000
        │   ├── file 1
        │   └── ...
        ├── 501000
        │   ├── file 1
        │   └── ...
        ├── 1000000
        │   ├── file 1
        │   └── ...
        ├── 5000000
        │   ├── file 1
        │   └── ...    
        ├── 10000000
        │   ├── file 1
        │   └── ...
        └── 10000000000
            ├── file 1
            └── ...
```

You can run the following command to begin to recover the master key : 

```bash
python3 decrypt.py
```
