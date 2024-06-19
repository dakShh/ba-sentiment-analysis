import os
import csv
import requests
from bs4 import BeautifulSoup
from app import config

base_url = "https://www.airlinequality.com/airline-reviews/british-airways"
pages = 5
page_size = 1000
reviews = []

if not os.path.exists(config.BASE_PATH):
    os.makedirs(config.BASE_PATHH)

def start_scraping():
    print("Scrapper started..")
    for i in range(1, pages + 1):

        print(f"Scraping page {i}")

        # Create URL to collect links from paginated data
        url = f"{base_url}/page/{i}/?sortby=post_date%3ADesc&pagesize={page_size}"

        # Collect HTML data from this page
        response = requests.get(url)

        # Parse content
        content = response.content
        soup = BeautifulSoup(content, 'html.parser')
        
        review_containers = soup.find_all("article",{"itemprop": "review"})

        for container in review_containers:
            rating_ele = container.find("span",{"itemprop":"ratingValue"})
            review_heading_ele = container.find("h2", {"class":"text_header"})
            time_ele = container.find("time", {"itemprop":"datePublished"})
            review_ele = container.find("div", {"itemprop":"reviewBody"})

            if rating_ele:
                rating = container.find("span",{"itemprop":"ratingValue"}).text
            else:
                rating = "404"
            
            
            if review_heading_ele:
                review_heading = container.find("h2", {"class":"text_header"}).text[1:-1]
            else:
                review_heading = "Na"

            if time_ele:
                time = container.find("time", {"itemprop":"datePublished"}).text
            else:
                time = "Na"

            if review_ele:
                review = container.find("div", {"itemprop":"reviewBody"}).text
            else:
                review = "Na"

            reviews.append(f"{rating.replace(",","")}, {review_heading.replace(",","")}, {time.replace(",","")}, {review.replace(",","")}")

        
        print(f"Number of reviews scrapped: {len(reviews)}")
        print("-"*45)



def view_all_reviews():
    for i in range(len(reviews)):
        print(reviews[i])
        print("-"*50)

# start_scraping()
# view_all_reviews()

def save_to_csv():
    filename = input("Enter name for the CSV file: ")
    with open(os.path.join(config.BASE_PATH, filename+".csv"), 'w', newline='',encoding='utf-8') as csvfile:
        
        # csv_writer = csv.writer(csvfile)
        csvfile.write('Rating, Review Title, Date, Reviews\n')
        csvfile.write('\n'.join(reviews))

        # for review in reviews:
            # csv_writer.writerow([review])

    print(f"Data saved to {filename}")

