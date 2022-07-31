# Task 2 - Upload files to yandex.disk by API 

import os
import pathlib
from pathlib import Path
import yadisk

data_2 = os.path.abspath("data_folder/999.txt")
yandex_token = os.path.abspath("token_folder/ya_token.txt")
folder_name = '/folder for files'
upload_file_name = 'text.txt'
upload_path = folder_name + '/' + upload_file_name

if __name__ == '__main__':
    with open (yandex_token, 'r') as token_file:
        ya_token = token_file.read().strip()
    y = yadisk.YaDisk(token=ya_token)
    print(y.check_token()) 
    y.mkdir(folder_name) 
    y.upload(data_2, upload_path) 
