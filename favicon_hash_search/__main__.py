import argparse
import base64
import mmh3
import requests


def get_opts():
    '''Get command line arguments
    '''
    parser = argparse.ArgumentParser(prog='favicon_hash_search',
                                     description='Get MurmurHash for '
                                     'favicons, to search Shodan.'
                                     )
    parser.add_argument('url')
    opts = parser.parse_args()
    return opts


# TODO: find out if possible automate favicon search in content bs4?


if __name__ == '__main__':
    # surpress InsecureRequestWarning: Unverified HTTPS request warning
    # from urllib3
    requests.packages.urllib3.disable_warnings(
        requests.packages.urllib3.exceptions.InsecureRequestWarning
        )
    opts = get_opts()
    url = opts.url
    # get the favicon
    response = requests.get(url, verify=False)
    # hash the favicon
    favicon = base64.encodebytes(response.content)
    ficon_hash = mmh3.hash(favicon)
    print('\n[***]Use the following query on Shodan:\n'
          f'http.favicon.hash:{ficon_hash}\n')
