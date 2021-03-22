from bs4 import BeautifulSoup
import requests
import pandas as pd

page = requests.get("https://www.detik.com/");
soup = BeautifulSoup(page.content, 'html.parser')

most_popular = soup.find(class_="cb-mostpop")

list_number = [lp.get_text() for lp in most_popular.select(".list-content__item .text-list__data ")]
list_title = [lt.get_text().replace('\n','') for lt in most_popular.select(".media__title")]
list_source = [ls.get_text() for ls in most_popular.select(".media__date")]

news = pd.DataFrame({
    "number" : list_number,
    "title" : list_title,
    "source" : list_source
})

news.to_csv(r'news.csv', index = False, header=True)

print(news)