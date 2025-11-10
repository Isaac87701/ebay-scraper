thonfrom bs4 import BeautifulSoup

def parse_product_page(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    product = {
        'url': soup.find('link', rel='canonical')['href'],
        'title': soup.find('h1', class_='x-item-title').text.strip(),
        'price': soup.find('span', class_='x-price-approx__price').text.strip(),
        'description': soup.find('div', class_='d-item-description').text.strip(),
        'image': soup.find('img', class_='x-product-image')['src'],
        'brand': soup.find('span', class_='d-item-brand').text.strip(),
        'categories': [category.text for category in soup.find_all('a', class_='d-item-category-link')]
    }
    return product