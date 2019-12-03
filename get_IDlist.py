import requests
import re

r = requests.get("https://www.gutenberg.org/wiki/Category:FR_Genre")

subdir_list = []

for line in r.text.split('\n'):
    if line.find('(Genre)">') != -1:
        subdir_list.append(line.split('"')[1])

ebook_id_list = []
for subdir in subdir_list:
    r = requests.get("https://www.gutenberg.org/" + subdir)
    for line in r.text.split('\n'):
        index_start = line.find('title="ebook:')
        if index_start != -1:
            index_stop = line.find('"', index_start + 13, len(line))
            ebook_id_list.append(int(line[index_start + 13:index_stop]))

#for ebook_id in ebook_id_list:
#   text = strip_headers(load_etext(2701)).strip()
# TO BE CONTINUED ...