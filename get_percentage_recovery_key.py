import os

DEBUG = False
total_letter = 0
total_match = 0

path_clean = ... #"./data/clear"
path_decrypt = ... #"./data/hived"

def transform_into_list_char(file):
    list_of_letters = []
    for line in file.readlines() :
        for letter in line:
            list_of_letters.append(letter)
    return list_of_letters

def find_file_decrypt(file_name_clear,path):
    # use only for debug reason
    for file in os.listdir(path):
        if file.startswith(file_name_clear):
            return file
def main():
    global total_match,total_letter
    global path_decrypt,path_clean

    for folder in os.listdir(path_clean):
        for filename in os.listdir(path_clean + '/' + folder):

            clean_file_path = path_clean+'/' + folder + '/' + filename
            if DEBUG:
                name_decrypt_file = find_file_decrypt(filename, path_decrypt+ '/' + folder)
                decrypt_file_path = path_decrypt+ '/' + folder + '/' + name_decrypt_file
            else:
                decrypt_file_path = path_decrypt+ '/' + folder + '/' + filename

            clean_file = open(clean_file_path,'br')
            decrypt_file = open(decrypt_file_path,'br')

            letter_clean = transform_into_list_char(clean_file)
            letter_decrypt = transform_into_list_char(decrypt_file)


            assert len(letter_clean) == len(letter_decrypt)

            total_letter += len(letter_decrypt)

            for idx in range(len(letter_clean)):
                if letter_clean[idx] == letter_decrypt[idx]:
                    total_match += 1
            #break
        #break

    print(f"Percentage of recovery: {total_letter/total_match}")

main()
