import requests
from bs4 import BeautifulSoup


def scrape_sports_data(url):
    try:
        # Send a GET request to the webpage
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Locate the sports section using its specific attributes
        sports_section = soup.find('div', {'aria-labelledby': 'Sport'})

        if not sports_section:
            print("Sports section not found.")
            return []

        # Extract sports-related visible text, preserving the list format
        sports_data = []
        items = sports_section.find_all('li')

        for item in items:
            # Extract visible text from each list item
            text = item.get_text(strip=True)
            if text:
                sports_data.append(f"- {text}")

        return sports_data

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while requesting the page: {e}")
        return []


url = "https://en.wikipedia.org/wiki/Portal:Current_events"
sports_content = scrape_sports_data(url)

if sports_content:
    print("Sports-related content found:")
    print("\n".join(sports_content))
else:
    print("No sports-related content found.")
