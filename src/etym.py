# !/usr/bin/env python

import argparse
import sys
sys.path.append('/Users/dietrichwambach/anaconda/lib/python2.7/site-packages')

from bs4 import BeautifulSoup

import utility  # local import

# GLOBALS
ETYMONLINE_URL = 'http://etymonline.com/index.php?'
# TODO handle all of the other options available at etymonline
# http://etymonline.com/index.php?allowed_in_frame=0&search=vocabword+&searchmode=none


def etym_term(term_keyword):
    """ Will request ETYMONLINE_URL + term_keyword, returns a *list* of search results """

    ret_list = []

    url_str = '{url}term={keyword}'.format(url = ETYMONLINE_URL, keyword = term_keyword)
    etym_document = utility.download_url(url_str)
    try:
        soup = BeautifulSoup(etym_document, 'lxml')
        dictionary_section = soup.find(id = 'dictionary')
        for etym_entry in dictionary_section.findChildren(name = 'dt'):
            entry_title = etym_entry.text.strip()
            entry_body = etym_entry.find_next_sibling().text.strip()
            entry = u'{title}:\n\t{body}'.format(title = entry_title, body = entry_body)
            ret_list.append(entry)
    except Exception as e:
        print e
        raise Exception('[!] Error when soupifying etym_document')
    return ret_list

if __name__ == '__main__':
    # Parse commandline arguments
    try:
        etym_arg_parser = argparse.ArgumentParser()
        etym_arg_parser.add_argument('term_word', help = 'Word to be researched.')
        etym_args = etym_arg_parser.parse_args()
    except Exception as e:
        print e
        raise Exception('[!] Error when parsing command line arguments')

    try:
        etym_entries = etym_term(etym_args.term_word)
    except Exception as e:
        print e
        raise Exception('[!] Error occurs when running etym_dump with term_word: {}'.format(etym_args.term_word))

    # Print out the results
    # print '\n' # create some space from command prompt
    for entry in etym_entries:
        print entry
        print '\n'
