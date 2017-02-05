import json
import re
import sys

import requests
from bs4 import BeautifulSoup

from store import Store, SteamException

regex_app_id = re.compile('app/([0-9]+)/')

start = 0
total_count = 0
steam_store = Store()

reviews = []

while True:
    result = requests.get('http://steamcommunity.com/groups/japanization/ajaxgetrecommendations/render/', params={
        'query': '',
        'start': start
    })

    print(result.url, file=sys.stderr)

    obj = json.loads(result.text)

    if not obj['success']:
        print(obj, file=sys.stderr)
        exit(-1)

    results_html = BeautifulSoup(obj['results_html'], 'lxml')

    for product in results_html.find_all(class_='curation_app_block'):
        app_id = int(regex_app_id.search(product.find(class_='curation_app_block_content').a['href']).group(1))
        app_name = product.find(class_='title').string.strip().replace(' - Recommended', '')
        summary = product.find(class_='curation_app_block_blurb').get_text().strip()

        try:
            link = product.find(class_='highlighted_recommendation_link').a['href']
        except Exception as e:
            print(e, file=sys.stderr)
            link = ''

        try:
            data = steam_store.appdetails(app_id)

            reviews.append({
                'steam_appid': app_id,
                'name': app_name,
                'review_summary': summary,
                'review_detail_link': link,
                'support_japanese_by_official': Store.support_japanese(data),
                'support_japanese_by_community': None,
                'header_image': data['header_image']
            })
        except SteamException:
            pass

    start += 10

    if start > obj['total_count']:
        break

print(json.dumps(reviews))
