import csv
import urllib.request

csv_mapping = {
    0: 'seq',  # SEQ
    2: 'name',  # 作品名
    3: 'mod_status',  # 日本語動作状態
    4: 'mod_category',  # カテゴリ
    5: 'mod_author',  # JPMOD 作者
    6: 'mod_workshop_name',  # 作業場 リンク名
    7: 'mod_workshop_link',  # 作業場 リンク
    8: 'mod_description',  # 備考
    9: 'mod_detail_link'  # 詳細ページURL
}

master_csv_url = 'https://docs.google.com/spreadsheets/d/15ZeN1KT0SyixMtzu9NZ_HGFdmNCksse88o7fkN_V27w/export?format=csv&id=15ZeN1KT0SyixMtzu9NZ_HGFdmNCksse88o7fkN_V27w&gid=0'


def map_dict(rows: list, mapping: dict):
    products = []

    for row in rows:
        product = {}

        for index, key in mapping.items():
            product[key] = row[index]

        products.append(product)

    return products


def read_csv(filename=None):
    if not filename:
        csv_file = urllib.request.urlopen(master_csv_url).read().decode().split('\r\n')
    else:
        csv_file = open(filename).readlines()

    reader = csv.reader(csv_file)
    next(reader)  # Skip first row

    return map_dict(list(reader), csv_mapping)


if __name__ == '__main__':
    pass
