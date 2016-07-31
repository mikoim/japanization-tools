import json
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage) {:s} 12345'.format(sys.argv[0]))
        exit(-1)

    appid = sys.argv[1]
    res = requests.get('http://localhost:8080/v1/store/appdetails/{:s}'.format(appid))
    result = json.loads(res.text)

    try:
        root = result[appid]['data']
        name = root['name']
        is_support_japanese = 'Yes' if 'Japanese' in root['supported_languages'] else 'No'
    except (KeyError, TypeError):
        name = 'Not Found'
        is_support_japanese = '?'

    print('\t'.join([name, is_support_japanese]))
