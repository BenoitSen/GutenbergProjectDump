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
#for ebook_id in ebook_id_list:
#   text = strip_headers(load_etext(ebook_id)).strip()