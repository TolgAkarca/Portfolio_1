import requests

def get_holidays(year, api_key, country="US"):
    url = f"https://holidayapi.com/v1/holidays?key={api_key}&country={country}&year={year}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data.get("holidays", [])
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

def print_holidays(holidays):
    for holiday in holidays:
        print(f"{holiday['date']} - {holiday['name']}")

def main():
    api_key = "77e0952e-ff08-477f-86d4-576fa9e91ecf"  
    year = 2022
    country = "US"

    holidays = get_holidays(year, api_key, country)

    if holidays:
        print_holidays(holidays)

if __name__ == "__main__":
    main()



response = requests.get('https://newsapi.org/v2/top-headlines?country=gb&apiKey=8ecab688183a4eaeafa8da3875630338')
data2 = response.json()
headlines = [article['title'] for article in data2['articles']]
print('\nTop Headlines:')
for i, headline in enumerate(headlines):
    print(i+1, headline)