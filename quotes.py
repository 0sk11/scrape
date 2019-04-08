import requests
from bs4 import BeautifulSoup
from csv import writer
counter = 1
while True:
	response = requests.get("http://quotes.toscrape.com/page/"+str(counter)+"/")
	soup = BeautifulSoup(response.text,"html.parser")
	quotes = soup.find_all(class_='quote')
	if quotes:
		for quote in quotes : 
			main_quote = quote.find(class_="text").get_text()
			author = quote.find(class_="author").get_text()
			with open('quotes.txt','a', encoding='utf-8') as file:
				file.write(main_quote)
				file.write("\n")
				file.write("\t")
				file.write(author)
				file.write("\n\n")
	counter +=1		

