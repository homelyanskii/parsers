
# coding: utf-8

# In[1]:


import requests
import sys
import re
from bs4 import BeautifulSoup
from time import sleep


# In[2]:


URL = 'https://www.menu.by/restaurant/pizza-lisitsa-lizy-chaykinoy.html'
HEADERS = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36', 'accept': '*/*'}
HOST = 'https://www.menu.by'


# In[3]:


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


# In[4]:


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('a', class_='title prod_content_a')

    product = []
    for item in items:
        item = re.sub(r'^#\d+\s*', '', item.get_text())
        product.append(item)
        print(item)
    return product


# In[5]:


def file_out(file, items):
    fout = open(file, "w", encoding='utf-8')
    for item in items:
        fout.write(item + '\n')
    fout.close()


# In[6]:


def parse():
    try:
        while(1):
            print('Try to get: {}'.format(URL))
            html = get_html(URL)
            status = html.status_code
            if status == 200:
                spisok = get_content(html.text)
                file_out('sushimaster_assortiment.txt', spisok)
                break
            else:
                sleep(1)
    except Exception:
        print(sys.stderr, 'Something went wrong... on stage {}'.format(i))
    except KeyboardInterrupt:
        print('Interrupted from keyboard on stage {}'.format(i))


# In[7]:

if __name__ = "__main__":
    parse()

