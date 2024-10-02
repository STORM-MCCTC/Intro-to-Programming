import requests as req
from bs4 import BeautifulSoup

url = "https://www.wunderground.com/weather/us/oh/youngstown"

response = req.get(url)

soup = BeautifulSoup(response.text, "html.parser")

print(f"status code: {response.status_code}")

# print(soup.prettify())

temperature_element = soup.find_all("span", class_="wu-value wu-value-to")

# temperature = temperature_element.text if temperature_element else "N/A"

for element in temperature_element:
    print(element.text)


# print(f"Curent temp: {temperature}")