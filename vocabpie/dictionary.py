#!/usr/bin/env python
import argparse
import sys
sys.path.append('/Users/dietrichwambach/anaconda/lib/python2.7/site-packages')

from bs4 import BeautifulSoup

import utility  # local import

# GLOBALS
DICTIONARY_URL = 'http://dictionary.reference.com/browse/'
# TODO handle all of the other options available at thesonline


def dict_term(term_keyword, antonym = False):
    """ Will request DICTIONARY_URL + term_keyword, returns a *list* of search results """

    ret_list = []

    url_str = '{url}{keyword}'.format(url = DICTIONARY_URL, keyword = term_keyword)
    dict_document = utility.download_url(url_str)
    try:
        soup = BeautifulSoup(dict_document, 'lxml')
        definition_section = soup.find('div', attrs = {'class': 'def-list'})
        definition_list = definition_section.find_all('div', attrs = {'class': 'def-content'})
        for dict_entry in definition_list:
            entry = dict_entry.text.strip()
            ret_list.append(entry)
    except Exception as e:
        print e
        raise Exception('[!] Error when soupifying dict_document')
    return ret_list


def run_dict():
    # Parse commandline arguments
    try:
        dict_arg_parser = argparse.ArgumentParser()
        dict_arg_parser.add_argument('term_word', help = 'Word to be researched.')
        dict_args = dict_arg_parser.parse_args()
    except Exception as e:
        print e
        raise Exception('[!] Error when parsing command line arguments')

    try:
        dict_entries = dict_term(dict_args.term_word)
    except Exception as e:
        print e
        raise Exception('[!] Error occurs when running dict_dump with term_word: {}'.format(dict_args.term_word))

    # Print out the results
    # print '\n' #create some space from command prompt
    for index in xrange(len(dict_entries)):
        def_str = dict_entries[index][0].upper() + dict_entries[index][1:]
        print '{i}. {d}\n'.format(i = index + 1, d = def_str)

if __name__ == '__main__':
    run_dict()
