import mariadb
import csv
import sys

try:
    conn = mariadb.connect(
        user="root",
        password="datanet",
        host="127.0.0.1",
        port=3306,
        database="base_datanet"
    )
except mariadb.Error as e:
    print(f"Ошибка подключения к MariaDB: {e}")
    sys.exit(1)

cur = conn.cursor()

with open('codes.txt', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    values_to_delete = [row[0] for row in reader]

for value in values_to_delete:
    cur.execute("DELETE FROM codes WHERE code_value = ?", (value,))

conn.commit()

conn.close()
