import requests
import re
# Search all or n_file_text_request french texts in the gutenberg project you can find here
#    https://www.gutenberg.org/wiki/Category:FR_Genre

n_file_text_request = 10
r = requests.get("https://www.gutenberg.org/wiki/Category:FR_Genre")

subdir_list = re.findall('/wiki/(.*)_\(Genre\)"', r.text, re.MULTILINE)

ebook_id_list = []
count_file_dump=0
for subdir in subdir_list:
    count_file_dump +=1
    if (count_file_dump >= n_file_text_request):
        break
    r = requests.get("https://www.gutenberg.org/wiki/" + subdir + "_(Genre)")
    e_ids = re.findall('title="ebook:([0-9]+)">', r.text, re.MULTILINE)
    ebook_id_list += e_ids
    
print('All French file text have been find')

# Write this files text in one file text
# You can get this on https://pypi.org/project/Gutenberg/
from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers


import io

for ebook_id in ebook_id_list:
    text = strip_headers(load_etext(int(ebook_id))).strip()
    with io.open('data_txt_gutenberg.txt', 'a', encoding='utf-8') as file:
        file.write(text) 

print('End of dump')