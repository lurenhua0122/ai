import requests
from bs4 import BeautifulSoup

# URL of the paper
url = "https://arxiv.org/abs/2308.08155"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Extract the title, abstract, and keywords
title = soup.find("h1", class_="title mathjax").text.strip()
abstract = soup.find("blockquote", class_="abstract mathjax").text.strip()
keywords = [tag.text.strip() for tag in soup.find_all("a", class_="tag")]

# Print the extracted information
print("Title:", title)
print("Abstract:", abstract)
print("Keywords:", keywords)