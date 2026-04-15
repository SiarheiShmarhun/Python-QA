"""XML module: calculating the cost of goods in a store."""

import logging
import xml.etree.ElementTree as ET
from os.path import exists

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


def calculate_total_price(filename: str) -> None:
    if not exists(filename):
        root = ET.Element('inventory')
        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8')
        logging.info("File %s was not found and was created as empty.", filename)
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        total = 0.0
        for product in root.findall('product'):
            price_node = product.find('price')
            quantity_node = product.find('quantity')
            if price_node is not None and quantity_node is not None:
                price_text = price_node.text
                quantity_text = quantity_node.text
                if isinstance(price_text, str) and isinstance(quantity_text, str):
                    total += float(price_text) * float(quantity_text)
        logging.info("Total cost of all products: %g", total)
    except (ET.ParseError, ValueError) as error:
        logging.error("Error processing data: %s", error)


if __name__ == "__main__":
    calculate_total_price("items.xml")
