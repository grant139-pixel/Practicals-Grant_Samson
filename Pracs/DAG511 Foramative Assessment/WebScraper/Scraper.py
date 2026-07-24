#Created by Grant Samson OCC:SD 1
#Student Number: 20261424
#Campus: CTU STellenbosch Campus
# Facilitator: Mr NB Dube
#what my code does is that it scrapes through the website and returns all the quotes their authors and the tags accociated with those quotes. 
# It also then turns that data into html data, then coverts it into a csv file and a json file for better data readability and understanding

import re #importing regex into the code

#importing all the neccessary libraries
from bs4 import BeautifulSoup
import requests

#importing csv
import csv

#importing json
import json

#importing pandas inorder to make my summary 
# reference: Python Programming program (2026),Pandas dataframe. Available at:https://realpython.com/pandas-dataframe/ [Accessed: 09/05/2026]
#reference: Available at: https://www.youtube.com/watch?v=6WW7J7Hhw8c Author: Programming knowledge [Acessed: 09/05/2026]
#reference: Available at: https://www.w3schools.com/python/pandas/pandas_getting_started.asp Author: W3schools [Acccessed:09/05/2026]
import pandas as pd

#Website Link
url="https://quotes.toscrape.com"

#try and except with response code mentioned
#Part 1
try:
    response = requests.get(url="https://quotes.toscrape.com")

    if response.status_code == 200:
        print("Website accessed successfully!")

        #the following print allows me to get the raw html code in the form of a text thus when i
        #print the response in .text format so i can copy it down and turn it into a .html file
        #print(response.text) 
        with open("raw.html","w", encoding="utf-8") as file:
            file.write(response.text)
            print("Raw HTML saved to raw.html successully!")
       # The code above displays the raw html code of the website which i then copied and put in raw.html
       #learnt from reference:Codehead01(2026), Webscraping with Python [Online video]Youtube Available at:https://www.youtube.com/watch?v=hHQlcnubuFI [Accessed: 05/05/2026]
        soup = BeautifulSoup(response.text, "html.parser")
        print("\nWebsite converted into soup successfully!\n")

        #Part 2 question six where i am asked to find all the repeated data elements(quotes)
        quotes=soup.find_all("div",class_="quotes")
        print("Page Title: ")
        print(soup.title.text)
        print("\nAmount of repeated elements: ") #heading that tells us what is going to be displayed underneath it

        #creating a list that stores all the quotes on all the pages of the website
        all_quotes=[]

        #finds all the quotes on the page
        quotes=soup.find_all("div", class_="quote")
        print(f"\nFound {len(quotes)} repeated quote elements") #got the idea to use the f-strings since it allows us to use embedded values/
        #reference:Joanna Jablonski (2026), Python f-strings Available at:https://realpython.com/python-f-strings/ [Accessed: 08/05/2026]
 
#Part 2 and 3
        #A while loop that continues to scrap the rest of the pages
        #referece:W3Schools (2026), Python While loops.  at:https://www.w3schools.com/python/python_while_loops.asp [Accessed:09/05/2026]
        while url: #this will continue to loop through the website as long as the url has a value and at the end becomes none when no value is assigned for the url meaning that there are no more pages that are being found within the website
            response = requests.get(url) #makes the request to the current page that it is trying to access, if the condition of status code 200 is met it converts the html into beautifulsoup objcects
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                quotes = soup.find_all("div", class_="quote") #after the html is turned into beautiful soup it finds all the quotes with <div> elements on the page and scrapes them
                print(f"Scraping: {url} - Found {len(quotes)} quotes")

                for a in quotes:
                    #reference:Zenva (2026), Webscraping with Beautifulsoup [Online Video] Youtube Available at:https://www.youtube.com/watch?v=4uuKtuFAKC0  [Accessed:08/05/2026]
                    #finds all the quotes
                    #This part loops and finds all the quotes on the page and extracts the text,authors and their tags then appends all that information within the list that i created called all_quotes 
                    #in addittion to this since the strip=true feauture is actvated when getting the text it removes and cleans up the coode whenever they are displayed in the terminal
                    text = a.find("span", class_="text").get_text(strip=True)
                    text = re.sub(r"[“”]", "", text) #using regex learnt in Reference:Kite (2026) Python regex tutorial [Online Video] Youtube Available at: https://www.youtube.com/watch?v=UQQsYXa1EHs [Accessed: 08/05/2026]
                    #finds all the authors
                    author = a.find("small", class_="author").get_text(strip=True)
                    #finds all the tags within each quote
                    tags = a.find_all("a", class_="tag")
                    #since there is multiple tags for certain quotes i created a list that gets looped and graps all the text and saves them within the list
                    tags_list = [tag.get_text(strip=True) for tag in tags]

                    #gathers all the info together so that they all show up in one line
                    data_quote = {"quotes": text, "author": author, "tags": ",".join(tags_list)}
                    all_quotes.append(data_quote)

                #this section of the loop checks if there is a "Next" button that exists on the specific page after it has been successfully been scraped
                #reference: GeeksforGeeks (2025), How to get the next page on BeautifulSOup? Available at: https://www.geeksforgeeks.org/python/how-to-get-the-next-page-on-beautifulsoup/ [Accessed: 10/05/2026]
                #referene: Richardson, L (2024), Beautiful soup Documentation. Available at:https://www.crummy.com/software/BeautifulSoup/bs4/doc/ [Accessed: 10/05/2026]
                next_button = soup.find("li", class_="next")
                if next_button:
                    next_url = next_button.find("a")["href"]
                    url = "https://quotes.toscrape.com" + next_url
                else:
                    url = None #if a next button is not found after a page has been scrapped this ends the loop
            else:
                print("Failed to access website")
                url = None

        print("Extracted Data:") #stores  all extracted items in a list of dictionaries a then prints them
        for x in all_quotes: #this for loop is applied so that the code keeps running through the dictonary until there are no more things to be read from those dictionaries
            print(f"Qoute: {x['quotes']}") #reference:W3Schools (2026),Python Dictonaries Available at: https://www.w3schools.com/python/python_dictionaries.asp [Accessed:09/05/2026]
            print(f"Author: {x['author']}")# i used the f string that allows me to easily turn objects into strings for easier readibility this way i can seperate the catergories and make them neat in accordance to my *all_quote* list
            print(f"Tags: {x['tags']}")
            print()


#part 4
        #exports to csv file reference:Codehead01 (2026), Web scarping with python [Online Video], Youtube Available at: https://www.youtube.com/watch?v=hHQlcnubuFI [Accessed:08/05/2026]
        #reference:Python Software Foundation (2026),csv- CSV file reading and writing Available at: https://docs.python.org/3/library/csv.html  [Accessed:08/05/2026]
        #reference:Jubal1961 (2020),Finding csv file to show data with vs code Available at: https://stackoverflow.com/questions/61575311/finding-csv-file-to-show-data-with-vs-code [Accessed:08/05/2025]
        #used the layout as a guideing tool
        with open("output.csv","w", newline="", encoding="utf-8") as file:
            fieldnames=["quotes","author","tags"] #defining the header row
            writer=csv.DictWriter(file,fieldnames=fieldnames) #creates a writer
            writer.writeheader() #writes ther header row
            writer.writerows(all_quotes)

            #prints a message if cvs creation was successfully exported
            print("\nData exported to output.csv successfully created!")

        #exports to json file reference:Python Software Foundation (2026),JSOn encoder and decoder Available at: https://docs.python.org/3/library/json.html [Accessed:08/05/2026]
        #referece:https:W3Schools (2026),Python JSON Available at: //www.w3schools.com/python/python_json.asp [Accessed:08/05/2026]
        with open("output.json", "w", encoding="utf-8") as file:
            json.dump(all_quotes, file, indent=4, ensure_ascii=False)   
            #prints a message if the json file was successfully exported 
            print("\nData exported to output.JSON successfully created!")

#part 5 Summary
#number of items scrapped
#reference: W3Schools (2026),Pandas DataFrames Available at: https://www.w3schools.com/python/pandas/pandas_dataframes.asp  [Accessed:09/05/2026]
        print("\n"+"="*30) #creted a border inorder to neatly display the heading and the \n makes sure that a line is skipped before the border is displayed
        print("     Summary of web scraping")
        print("="*30)
        df=pd.DataFrame(all_quotes) #referenced at the top
        print(f"Number of items scrapped: {len(df)}") #Summary of the total number of items that were scrappe using this code by going through the length of the list that id created to store all the quotes that are within the website itself 
        e=df['author'].value_counts().idxmax() #Returns the name of the author whos name appears the most
        print(f"Most common author is: {e}")#reference:TechinicallyRipped (2026), Pandas idxmax [Online Video], Youtube Available at: https://www.youtube.com/shorts/w845hzVhIzk [Accesssed:09/05/2026]
        g=df['tags'].value_counts().idxmax() #returns the tag that appears the most
        print(f"Tag that appears the most is: {g}")
        h=df['author'].nunique()#using the unique function to get unique values in the defined DataFrame
        print(f"Number of unique Authors is: {h}")#reference:IONOS Editorial Team (2025), Pandas unique function Available at: https://shorturl.at/gP4ZS [Accessed:09/08/2026]
        i=df['tags'].nunique()
        print(f"The Number of unique tags is: {i}")
        t=df['author'].apply(len).mean() #reference:Python Software Foundation (2026),Pandas dataframe mean html Available at: https://pandas.pydata.org/pandas-docs/dev/reference/api/pandas.DataFrame.mean.html [Accessed:09/05/2026]
        print(f"The average length of Author names is: {t: .0f}")#using the apply(len) function because the authors names are in letters so this counts the number of letters 
        #each authors names contains and returns a value then afterwards it will get a mean from the list once it has looped around it
        #.0f allows me to round of my average off to the nearset whole number instead of leaving it as point(.) something
        
    else:# this is an else statement that displays a message if the response_code that was given by the website does not match that of the code written, especially when we get a 405, 402 or 400 response code meaning that the conditions set in the code wer failed to be met by the website
        print("Failed to access website!")
except Exception as e:
    print("An error occured")
    print(e)
