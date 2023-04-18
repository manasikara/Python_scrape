# learning sourse --> https://www.youtube.com/watch?v=XVv6mJpFOb0

from bs4 import BeautifulSoup

with open('about.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    tags = soup.find('h1')

    print(tags)
    
  
  # to be continued....