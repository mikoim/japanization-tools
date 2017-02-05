import json
import sys
import time

import requests


class SteamException(Exception):
    pass


class Store(object):
    l = None
    cc = None

    def __init__(self, language='en', country='jp'):
        self.l = language
        self.cc = country

    def appdetails(self, app_id: int) -> dict:
        url = 'http://store.steampowered.com/api/appdetails'
        cache_file_path = 'cache/{:d}.json'.format(app_id)
        api_str = str(app_id)

        try:
            with open(cache_file_path) as cached:
                return json.load(cached)[api_str]['data']
        except IOError:
            print('app_id = {:d} is not cached'.format(app_id), file=sys.stderr)

        time.sleep(2)
        r = requests.get(url=url, params={'l': self.l, 'cc': self.cc, 'appids': app_id})

        if r.status_code != 200:
            raise SteamException('Steam API returned non-200 status')

        j = r.json()

        if api_str not in j or not j[api_str]['success']:
            raise SteamException('Steam API returned unexpected error')

        with open(cache_file_path, mode='w') as cached:
            cached.write(r.text)

        return j[api_str]['data']

    @staticmethod
    def support_japanese(data: dict) -> bool:
        k = 'supported_languages'
        return k in data and 'Japanese' in data[k]
