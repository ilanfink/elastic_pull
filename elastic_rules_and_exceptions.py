#reworking for elastic exceptions list

import requests
import json

def get_rules():
    url = "elastic_url_goes_here:9243/api/detection_engine/rules/_find?per_page=200"

    payload = {}
    headers = {
        'Authorization': 'creds/go/here'
    }

    response = requests.request("GET", url, headers=headers, data=payload, timeout=100)

    with open('rules.ndjson', 'wb') as f:
        for line in response:
            f.write(line)


def get_exceptions_list():

    url = "elastic_url_goes_here:9243/api/exception_lists/_find?&page=1&per_page=2000"

    payload={}
    headers = {
        'Authorization': 'creds/go/here'
    }

    response = requests.request("GET", url, headers=headers, data=payload, timeout=1000)

    with open('exception_list.ndjson', 'wb') as e_list:
            for line in response:
                e_list.write(line)


def get_exception_values():



    with open('exception_list.ndjson', 'r') as t:
        vals = json.load(t)
        exception_vals = [e["list_id"] for e in vals["data"]]

    for i in exception_vals:
        url = f'https://elastic_url_goes_here:9243/api/exception_lists/items/_find?list_id={i}&namespace_type=single&page=1&per_page=2000&sort_field=exception-list.created_at&sort_order=desc'

        payload={}
        headers = {
        'Authorization': 'creds/go/here'
        }

        response = requests.request("GET", url, headers=headers, data=payload, timeout=100)

        with open('exceptions.ndjson', 'ab') as q:
            for line in response:
                q.write(line)
def main():
    get_rules()
    get_exceptions_list()
    get_exception_values()

if __name__ == "__main__":
    main()
