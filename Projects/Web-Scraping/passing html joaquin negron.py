import bs4
import requests
website = requests.get('https://forecast.weather.gov/MapClick.php?lat=37.849920000000054&lon=-119.56766999999996#.Yks29jUpBEY')
forecast = bs4.BeautifulSoup(website.content, 'html.parser')
sevenDay = forecast.find(id="seven-day-forecast")
forecast_items = sevenDay.find_all(class_="tombstone-container")
tonight = forecast_items[1]
# print(tonight.prettify())
period = tonight.find(class_="period-name").get_text()
print(period)
shortDesc = tonight.find(class_="short-desc").get_text()
print(shortDesc)
tempLow = tonight.find(class_="temp-low").get_text()
print(tempLow)