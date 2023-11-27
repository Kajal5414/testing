import requests
from bs4 import BeautifulSoup

def is_url_safe(url):
    url = "https://www.urlvoid.com/scan/" + url  # append the URL to the base URLVoid scan URL
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        result_div = soup.select_one("#scanned > div:first-child")
        if result_div:
            result = result_div.get_text().strip()
            return result != "not_safe"
        else:
            print("Unable to parse the response.")
    else:
        print("Error occurred while fetching the URL.")

# Example usage
url = input("Enter the URL to check: ")
safe = is_url_safe(url)

if(is_url_safe(url) == True):
    print("The URL is safe.")
else:
    print("The URL is potentially unsafe.")
print("Please enter another URL")