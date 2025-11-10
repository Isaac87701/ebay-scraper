thonimport re

def clean_price(price_str):
    return re.sub(r'[^\d.]', '', price_str)

def clean_title(title_str):
    return title_str.strip().replace("\n", " ")

def is_valid_price(price):
    try:
        float(price)
        return True
    except ValueError:
        return False