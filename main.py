import requests
import json

with open('sites.json', 'r') as file:
    data = json.load(file)

SITES = data['sites']

if __name__ == "__main__":
    for site in SITES:
        requests.get(site)
