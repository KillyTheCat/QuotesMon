from bs4 import BeautifulSoup
import requests
import random

pagenumber = random.randrange(1,100)

print(pagenumber)

url = "https://www.goodreads.com/quotes"+"?page="+str(pagenumber)

webdata = requests.get(url)
soup = BeautifulSoup(webdata.content,'html5lib')
text_data = soup.get_text()

quotes = []

table = soup.find('div', attrs= {"class":"quotes"})

for row in table.find_all('div', attrs={"class":"quoteText"}):
    text_data = row.text
    quotes.append(text_data)

print(random.choice(quotes))

#list = re.findall(r'"([^"]*)"', text_data)

#for i in list:
#    print(i)