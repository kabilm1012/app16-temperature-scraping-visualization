from webscrape import scrape, extract
from database_handling import store
import time


#PATH = "temp_data.txt"
URL = "https://programmer100.pythonanywhere.com/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

if __name__ == "__main__":
    while True:
        scraped = scrape(URL, HEADERS)
        extracted = extract(scraped)
        
        datetime = time.strftime(r"%Y/%m/%d - %H:%M:%S")
        store(datetime, extracted)
        print(datetime, extracted)

        time.sleep(2)
    