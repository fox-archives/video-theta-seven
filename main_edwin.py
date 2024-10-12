#!/usr/bin/env python3
import re
import requests
import json

search_str = 'apple'
debug = True

company_list = []
with open('./data/company_tickers_pretty.json') as f:
    contents = f.read()
    json_data = json.loads(contents)
    for entry in json_data['entries']:
        company_list.append(entry)

# r = requests.get()
# print(company_list)

found_company = None
for company in company_list:
    # if debug:
    #     print(company['title'].lower())

    if search_str.lower() in company['title'].lower():
        found_company = company
        break

if found_company == None:
    raise ValueError('Failed to find company')


print(company)
