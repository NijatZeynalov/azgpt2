"""
kishiyev, 23.02.2023
"""
import requests
from bs4 import BeautifulSoup
import io
from urllib.request import urlopen

url = 'https://kitabadasi.wordpress.com/elektron-kitabxana/'

def test(url):
    """
     Test case to check if url is valid.
     Input: URL (preferably string)
     Output: Validity
    """
    try:
        urlopen(url)
        print("Output successful.")
    except IOError:
        print("Output failed.")


response = requests.get(url)
bs = BeautifulSoup(response.text,'html.parser')
# features=lxml is a good idea too, but didn't work well for me

all_urls = bs.find_all('a') #to find all anchor html tags

pdf_urls = [] #an empty list to add url's at every iteration
for url in all_urls:
    try:
        if 'aze.pdf' in url['href'] or 'az.pdf' in url['href']: #condition to check if reference links are in Azerbaijani
            pdf_url = ''
            if'https' not in url['href']:
                pdf_url = 'https://kitabadasi.wordpress.com/elektron-kitabxana/' + url['href']
            else:
                pdf_url = url['href']

            print(pdf_url)
       
    except Exception as e: #Thrown exception to see what could go wrong
        print('Error:', e)


