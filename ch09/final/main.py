import requests


response1 = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&appid=8af98df4aac7bf07c8fd99324d643b26')
data1 = response1.json()


response2 = requests.get('https://newsapi.org/v2/top-headlines?country=gb&apiKey=8ecab688183a4eaeafa8da3875630338')
data2 = response2.json()


weather_desc = data1['weather'][0]['description']
weather_temp = data1['main']['temp'] - 273.15


headlines = [article['title'] for article in data2['articles']]


print('Current Weather in London:', weather_desc)
print('Temperature:', round(weather_temp, 2), 'degrees Celsius')
print('\nTop Headlines:')
for i, headline in enumerate(headlines):
    print(i+1, headline)