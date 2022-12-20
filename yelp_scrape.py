import re
import requests
from bs4 import BeautifulSoup
import pprint

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
    output=[]
    for review in all_reviews:
        author = review.find(class_='css-1m051bw').text
        stars = 5 - len(review.find_all(attrs={'fill':'#BBBAC0','opacity':'0.5','d':'M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z'}))
        date = review.find(class_='css-chan6m').text.replace('/','-')
        description = review.find(class_='raw__09f24__T4Ezm').text
        output.append({'author':author,'stars':stars,'date':date,'description':description})
    return output


def extract_yelp_reviews(url):
    output=[]
    for i in range(0,999,10):
        new_url= url + f'?start={i}'
        single_page_reviews = parse_yelp_page(new_url)
        output+=single_page_reviews
    return output


extract_yelp_reviews(URL)