import requests
from selectolax.parser import HTMLParser

base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
current_page = 1

while True:
    # Make a GET request to the current page
    response = requests.get(base_url.format(current_page))

    # Parse the HTML content
    parser = HTMLParser(response.content)

    # Find all the book items on the current page
    books = parser.css('article.product_pod')

    # Extract the prices and titles of all the books on the current page
    prices = [book.css_first('p.price_color').text(strip=True) for book in books]
    titles = [book.css_first('h3 > a').attrs.get('title') for book in books]

    # Print the prices and titles of all the books on the current page
    for i in range(len(prices)):
        print(f"Title: {titles[i]}\nPrice: {prices[i]}\n")

    # Check if there is a next page
    next_page = parser.css_first('li.next > a')
    if next_page is None:
        break
    else:
        current_page += 1

print('♨o(>_<)o♨ DinnerTime')
