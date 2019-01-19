from bs4 import BeautifulSoup
import requests

html = requests.get('https://ridibooks.com/category/bestsellers/2200').text
soup = BeautifulSoup(html, 'html.parser')


tag_list =[]
print('---------------')
for tag in soup.select('.title_link > .title_text'):
    #print(tag.text)
    if tag:
        x = tag.text
        tag_list.append(x.strip())
f = open('ridi.csv', 'w')
k = 0
for tag in tag_list:
    k += 1
    f.write(str(k) +'. ' + tag + '\n')
f.close()
