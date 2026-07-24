#created by grant and aiden


from bs4 import BeautifulSoup
import requests
import pandas as pd

url="https://books.toscrape.com/"

response=requests.get(url)

soup=BeautifulSoup(response.text,"html.parser")

books=soup.find_all('article', class_='product_pod')

book_data=[]

for book in books:
    title=book.h3.a['title']
    price=book.find('p', class_='price_color').text
    availability=book.find('p', class_='instock availability').text.strip()
    rating = book.find('p', class_='star-rating')['class'][1]
    book_data.append([title,price,availability,rating])
    

df=pd.DataFrame(book_data, columns=['Title','Price','Availability','Rating'])

print(df)

df.to_csv('books.csv',index=False)