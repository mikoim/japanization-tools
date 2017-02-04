from bs4 import BeautifulSoup
import requests
import json
import re
import sys

regex_app_id = re.compile('app/([0-9]+)/')

start = 0
total_count = 0

while True:
    result = requests.get('http://steamcommunity.com/groups/japanization/ajaxgetrecommendations/render/', params={
        'query': '',
        'start': start
    })

    print(result.url, file=sys.stderr)

    obj = json.loads(result.text)

    if not obj['success']:
        print(obj, file=sys.stderr)
        exit()

    results_html = BeautifulSoup(obj['results_html'], 'lxml')

    for product in results_html.find_all(class_='curation_app_block'):
        app_id = regex_app_id.search(product.find(class_='curation_app_block_content').a['href']).group(1)
        app_name = product.find(class_='curation_app_block_name').string.strip()
        summary = product.find(class_='curation_app_block_blurb').get_text().strip()

        try:
            link = product.find(class_='highlighted_recommendation_link').a['href']
        except:
            link = ''

        print('\t'.join([app_id, app_name, summary, link]))

    start += 5
    if start > obj['total_count']:
        break
