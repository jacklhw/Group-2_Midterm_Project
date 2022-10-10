import os
from scrape_ranking_pages import scrape_all_pages
import pandas as pd

# Function: scraping
def scrape(url):
    all_years = [2022]
    top=30
    all_data = pd.DataFrame(scrape_all_pages(url,all_years,top))
    all_data.sort_values(["year","rank"],inplace=True)
    return all_data

# Output to CSV
def output_to_csv(all_data, path):

    all_data.to_csv(path,header=True, index = False)
    return

def exe_scrape_ranking():
    all_data = pd.DataFrame({"id":{},"year":[],"rank":[], "name":[], "team":[],"salary":[],"player_url":[]},index=[])
    BASE_URL = "http://www.espn.com/nba/salaries"
    BASE_DIR = "artifacts"
    CSV_PATH = os.path.join(BASE_DIR, "results_ranking.csv")
    os.makedirs(BASE_DIR, exist_ok=True)
    all_data = scrape(BASE_URL)
    output_to_csv(all_data, CSV_PATH)