thonimport requests
from bs4 import BeautifulSoup
import csv
import json
import xml.etree.ElementTree as ET
import pandas as pd
import os

# Configuration settings
PROXY = "your_proxy_here"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

headers = {
    'User-Agent': USER_AGENT
}

def fetch_ebay_page(url):
    response = requests.get(url, headers=headers, proxies={"http": PROXY, "https": PROXY})
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch the page, status code {response.status_code}")

def parse_ebay_page(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    items = []
    product_containers = soup.find_all('li', class_='s-item')
    
    for product in product_containers:
        item = {
            'url': product.find('a', class_='s-item__link')['href'],
            'title': product.find('h3', class_='s-item__title').text,
            'price': product.find('span', class_='s-item__price').text,
            'image': product.find('img', class_='s-item__image-img')['src'],
            'seller': product.find('span', class_='s-item__seller-info-text').text.strip(),
        }
        items.append(item)
    
    return items

def save_data(items, output_format='json'):
    if output_format == 'json':
        with open('output.json', 'w') as f:
            json.dump(items, f, indent=4)
    elif output_format == 'csv':
        keys = items[0].keys()
        with open('output.csv', 'w', newline='') as f:
            dict_writer = csv.DictWriter(f, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(items)
    elif output_format == 'xml':
        root = ET.Element('items')
        for item in items:
            item_elem = ET.SubElement(root, 'item')
            for key, value in item.items():
                sub_elem = ET.SubElement(item_elem, key)
                sub_elem.text = value
        tree = ET.ElementTree(root)
        tree.write('output.xml')
    elif output_format == 'excel':
        df = pd.DataFrame(items)
        df.to_excel('output.xlsx', index=False)

if __name__ == "__main__":
    url = input("Enter eBay URL to scrape: ")
    page_html = fetch_ebay_page(url)
    items = parse_ebay_page(page_html)
    output_format = input("Enter output format (json, csv, xml, excel): ")
    save_data(items, output_format)