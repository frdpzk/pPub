import threading
import requests
from time import sleep
from pytz import timezone
from datetime import datetime, timedelta
import time
import asyncio
import aiohttp
from github import Github
from datetime import datetime
from ast import literal_eval
from secrets import choice
import json
import cloudscraper

scraper = cloudscraper.create_scraper(
    browser={
        'browser': 'chrome',
        'platform': 'windows',
        'desktop': True
    }
)
while 1:
    # x = scraper.get('https://api.bitpin.ir/v2/mth/actives/1/?type=buy').json()
    x = scraper.get('https://api.bitpin.ir/v2/mth/actives/1/?type=buy').json()
    print(x)
# for i in x['results']:
#     print(i)

# [https://api.bitpin.ir/v2/mth/actives/1/?type=buy, https://api.bitpin.ir/v2/mth/actives/1/?type=sell]
