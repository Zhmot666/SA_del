import json


def extract_barcodes(data, barcodes_list):
    if isinstance(data, dict):
        for key, value in data.items():
            if key == 'Barcode' and isinstance(value, str) and len(value) == 85:
                barcodes_list.append(value)
            else:
                extract_barcodes(value, barcodes_list)
    elif isinstance(data, list):
        for item in data:
            extract_barcodes(item, barcodes_list)


with open('codes.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

barcodes_list = []

extract_barcodes(data, barcodes_list)

with open('codes.txt', 'w', encoding='utf-8') as txt_file:
    for barcode in barcodes_list:
        txt_file.write(barcode + '\n')
