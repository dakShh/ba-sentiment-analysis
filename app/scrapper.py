import os
import csv
import requests
from bs4 import BeautifulSoup

base_url = "https://www.airlinequality.com/airline-reviews/british-airways"
pages = 1
page_size = 5

reviews = []

data_folder_path = "C:/engineered_actions/ml_projects/ba_sentiment_analysis/data"

if not os.path.exists(data_folder_path):
    os.makedirs(data_folder_path)

def start_scraping():
    for i in range(1, pages + 1):

        print(f"Scraping page {i}")

        # Create URL to collect links from paginated data
        url = f"{base_url}/page/{i}/?sortby=post_date%3ADesc&pagesize={page_size}"

        # Collect HTML data from this page
        response = requests.get(url)

        # Parse content
        content = response.content
        parsed_content = BeautifulSoup(content, 'html.parser')
        for para in parsed_content.find_all("div", {"class": "text_content"}):
            reviews.append(para.get_text())
        
        print(f"   ---> {len(reviews)} total reviews")

def view_all_reviews():
    for i in range(len(reviews)):
        print(reviews[i])
        print("-"*50)
    
def save_to_csv():
    # Open the CSV file in write mode with newline='' to avoid extra blank lines
    with open(os.path.join("C:/engineered_actions/ml_projects/ba_sentiment_analysis/data", "ba_reviews.csv"), 'w', newline='',encoding='utf-8') as csvfile:
        # Create a CSV writer object
        csv_writer = csv.writer(csvfile)

        # Write the data to the CSV file
        for row in reviews:
            csv_writer.writerow([row])

    print("Data saved to data.csv")