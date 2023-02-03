import requests
import json
from bs4 import BeautifulSoup

url = 'https://metro.co.uk/2023/02/02/british-gas-to-stop-using-warrants-to-force-prepay-meters-on-people-18209919/'

# Send a GET request to load the URL
response = requests.get(url)

# Parse the HTML content of the response
soup = BeautifulSoup(response.text, 'html.parser')

# Get the webpage headline
headline = soup.find('h1').text

# Get the author
author = soup.find(class_='author').text

# Get the Post date
date = soup.find(class_='post-date').text

# Get all image elements
images = soup.find_all('img')

# Initialize an empty list to store the image information
imageData = []

# Loop through each image
for img in images:
    # Get the image URL
    imgUrl = img.get('src')

    # Get the image caption
    imgCaption = img.get('alt')
    
    # Get the image credit
    imgCredit = img.get('credit')
    
    # Add the image information to the list
    imageData.append({'URL': imgUrl, 'Caption': imgCaption, 'Credit': imgCredit})

# Combine all the extracted information into a dictionary
data = {'Headline': headline, 'Author': author, 'Date': date, 'Images': imageData}

# Write the data to a JSON file
with open('output.json', 'w') as file:
    json.dump(data, file, indent=4)

print('Data written to output.json')
