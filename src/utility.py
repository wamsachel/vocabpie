#!/usr/bin/env python
import requests


def download_url(url):
    """ Download url, returns the contents of url as a string """
    ret_val = ''
    try:
        r = requests.get(url)
        ret_code = r.status_code
        if ret_code == 200:
            ret_val = r.text
        else:
            print '[!] {code} returned when requesting {url}'.format(code = ret_code, url = url)
    except Exception as e:
        print e
        raise Exception('[!] Error occurs when requesting {url}'.format(url))
    return ret_val
