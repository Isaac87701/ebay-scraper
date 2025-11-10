thonimport json
import csv
import xml.etree.ElementTree as ET
import pandas as pd

def export_to_json(data, file_name='output.json'):
    with open(file_name, 'w') as f:
        json.dump(data, f, indent=4)

def export_to_csv(data, file_name='output.csv'):
    if data:
        keys = data[0].keys()
        with open(file_name, 'w', newline='') as f:
            dict_writer = csv.DictWriter(f, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)

def export_to_xml(data, file_name='output.xml'):
    if data:
        root = ET.Element('items')
        for item in data:
            item_elem = ET.SubElement(root, 'item')
            for key, value in item.items():
                sub_elem = ET.SubElement(item_elem, key)
                sub_elem.text = value
        tree = ET.ElementTree(root)
        tree.write(file_name)

def export_to_excel(data, file_name='output.xlsx'):
    if data:
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)