'''
from bs4 import BeautifulSoup
import requests
from datetime import datetime

url = "http://www.daum.net/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
rank = 1

results = soup.findAll('a','link_favorsch')

search_rank_file = open("rankresult.txt","a")

print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))

for result in results:
    search_rank_file.write(str(rank)+"위:"+result.get_text()+"\n")
    print(rank,"위 : ",result.get_text(),"\n")
    rank += 1


import requests
from bs4 import BeautifulSoup
from datetime import datetime

print(requests)
print(requests.get)

url = "http://www.daum.net/"

response = requests.get(url)
print(response.text)

print(response.url)
print(response.content)
print(response.encoding)
print(response.headers)
print(response.json)
print(response.links)
print(response.ok)
print(response.status_code)

print(BeautifulSoup(response.text, 'html.parser'))

print(type(response.text))
print(type(BeautifulSoup(response.text, 'html.parser')))

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title)
print(response.text[:500])
print(soup.title.string)
print(soup.span)
print(soup.findAll('span'))

file = open("daum.html", "w")
file.write(response.text)
file.close()

results = soup.findAll("a", "link_favorsch")
print(results)

search_rank_file = open("rankresult.txt", "w")

rank = 1
print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))

for result in results:
    search_rank_file.write(str(rank)+"위:"+result.get_text()+"\n")
    print(rank, "위 : ", result.get_text(), "\n")
    rank =+ 1
'''
from bs4 import BeautifulSoup
import requests
from datetime import datetime

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = "http://datalab.naver.com/keyword/realtimelist.naver?age=20s"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
rank = 1

results = soup.findAll('span','itme_title')

print(response.text)

search_rank_file = open("rankresult.txt","a")

print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))

for result in results:
    search_rank_file.write(str(rank)+"위:"+result.get_text()+"\n")
    print(rank,"위 : ",result.get_text(),"\n")
    rank += 1
