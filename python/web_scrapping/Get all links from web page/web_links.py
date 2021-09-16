import requests
from bs4 import BeautifulSoup

url = input("Website link: ")
if ("https" or "http") in url:
    data = requests.get(url)
else:
    data = requests.get("https://" + url)
soup = BeautifulSoup(data.text, "html.parser")
links = []
for link in soup.find_all("a"):
    links.append(link.get("href"))

# Writing the output to a file (myLinks.txt) instead of to stdout
# You can change 'a' to 'w' to overwrite the file each time
with open("links.txt", 'a') as saved:
    print(links[:10], file=saved)