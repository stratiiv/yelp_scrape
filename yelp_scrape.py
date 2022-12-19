import re
import requests
from bs4 import BeautifulSoup

URL = 'https://www.yelp.com/biz/the-porch-at-schenley-pittsburgh'



def parse_yelp_page(url):
    """
    Parse the reviews on a single page of a restaurant.
    
    Args:
        url (string): URL string corresponding to a Yelp restaurant

    Returns:
        tuple(list, int): a tuple of two elements
            first element: list of dictionaries corresponding to the extracted review information
            second element: Number of pages total
    """
    
    # To use downloaded data, replace any command (or any equivalent using requests)
    # html = retrieve_html(url)[1]
    # with the command:
    # html = parse_yelp_page_dict[url]

    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')
    all_reviews = soup.find_all(class_='review__09f24__oHr9V border-color--default__09f24__NPAKY')
    for i in all_reviews:
        print()
parse_yelp_page(URL)