'''
Python requests module has several built-in methods to make HTTP requests to specified URI using GET, POST, PUT, PATCH, or HEAD requests. A HTTP request is meant to either retrieve data from a specified URI or to push data to a server. It works as a request-response protocol between a client and a server. Here we will be using the GET request. !pip install requests


GET method is used to retrieve information from the given server using a given URI. The GET method sends the encoded user information appended to the page request. !pip install requests

pip install requests

pip install beautifulsoup4

'''

import requests

# Making a GET request to a specified URL
r = requests.get('https://www.theknowledgeacademy.com/in/blog/what-are-the-benefits-of-coding/')

# Print the URL of the request object
print(r.url)

# Checking the status code of the response received
# A status code of 200 indicates success
print(f"Response Status Code: {r.status_code}")

# Printing the content of the response
# This prints the HTML content of the web page
print(r.content)

import requests
from bs4 import BeautifulSoup


# Making a GET request
# 
r = requests.get('https://www.theknowledgeacademy.com/in/blog/what-are-the-benefits-of-coding/')

# Check status code for response received
# Success code - 200
print(r)

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())
