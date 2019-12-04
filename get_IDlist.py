import requests
import re

r = requests.get("https://www.gutenberg.org/wiki/Category:FR_Genre")

subdir_list = re.findall('/wiki/(.*)_\(Genre\)"', r.text, re.MULTILINE)

ebook_id_list = []
for subdir in subdir_list:
    r = requests.get("https://www.gutenberg.org/wiki/" + subdir + "_(Genre)")
    e_ids = re.findall('title="ebook:([0-9]+)">', r.text, re.MULTILINE)
    ebook_id_list += e_ids
    print(ebook_id_list)

# TODO: Download the books thanks to the ebook id
from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers

file = open('data_txt_gutenberg.txt', 'wb')
i = 10
for ebook_id in ebook_id_list:
    text = strip_headers(load_etext(ebook_id)).strip()
    file.write(text)  
    i-=1
    if i==0:
        break
print('End of dump')

file.close()