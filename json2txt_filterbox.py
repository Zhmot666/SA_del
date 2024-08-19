import json


def extract_barcodes(data, parent_barcodes, valid_barcodes):
    if isinstance(data, dict):
        for key, value in data.items():
            if key == 'Barcode' and isinstance(value, str) and len(value) == 85:
                if parent_barcodes in box_codes:
                    valid_barcodes.append(value)
            else:
                if key == 'Barcode' and isinstance(value, str):
                    parent_barcodes = value
                extract_barcodes(value, parent_barcodes, valid_barcodes)
    elif isinstance(data, list):
        for item in data:
            extract_barcodes(item, parent_barcodes, valid_barcodes)


# Чтение значений из файла box_codes.txt
with open('box_codes.txt', 'r', encoding='utf-8') as file:
    box_codes = {line.strip() for line in file}

# Открываем JSON-файл для чтения
with open('codes.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Список для хранения найденных баркодов
valid_barcodes = []

# Извлекаем баркоды
extract_barcodes(data, "", valid_barcodes)

# Открываем текстовый файл для записи
with open('codes.txt', 'w', encoding='utf-8') as txt_file:
    for barcode in valid_barcodes:
        txt_file.write(barcode + '\n')
