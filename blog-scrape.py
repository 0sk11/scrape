import requests # to send requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://www.rithmschool.com/blog') # sending a get request to a site
# print(response.text) #.text will give back the html 
soup = BeautifulSoup(response.text,'html.parser') #response.text is the text sent back by request.get()
articles = soup.find_all('article')

with open("blog.csv","w") as csv_file:
	csv_writer = writer(csv_file)
	csv_writer.writerow(['date','title','url'])
	for article in articles:
		a_tag = article.find('a')
		title = a_tag.get_text()
		url = f"https://www.rithmschool.com{a_tag['href']}"                                                                            
		date = article.find('time')['datetime']
		csv_writer.writerow([date,title,url])