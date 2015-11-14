# !/usr/bin/env python

import argparse
import sys
sys.path.append('/Users/dietrichwambach/anaconda/lib/python2.7/site-packages')
import utility  # local import

from bs4 import BeautifulSoup

# GLOBALS
THESAURUS_URL = 'http://www.thesaurus.com/browse/'
# TODO handle all of the other options available at thesonline


def thes_term(term_keyword, antonym = False):
    """ Will request THESAURUS_URL + term_keyword, returns a *list* of search results """

    ret_list = []

    url_str = '{url}{keyword}'.format(url = THESAURUS_URL, keyword = term_keyword)
    thes_document = utility.download_url(url_str)
    try:
        soup = BeautifulSoup(thes_document, 'lxml')
        synonym_section = soup.find(id = 'synonyms-0')
        for thes_entry in synonym_section.findChildren(name = 'a'):
            # Every synonym entry has \nstar on the text, every antonym does not
            entry0 = thes_entry.text.strip().split('\n')
            entry = entry0[0]
            entry0_len = len(entry0)
            if entry0_len == 1 and antonym is True:
                    ret_list.append(entry)
            elif entry0_len == 2 and antonym is False:
                if 'star' in entry0[1]:
                    ret_list.append(entry)
    except Exception as e:
        print e
        raise Exception('[!] Error when soupifying thes_document')
    if 'Cite This Source' in ret_list[-1]:
        ret_list.pop()
    return ret_list

if __name__ == '__main__':
    # Parse commandline arguments
    try:
        thes_arg_parser = argparse.ArgumentParser()
        thes_arg_parser.add_argument('term_word', help = 'Word to be researched.')
        thes_arg_parser.add_argument('-a', '--antonym', action = 'store_true', help = 'Return the antonym of the word')
        thes_args = thes_arg_parser.parse_args()
    except Exception as e:
        print e
        raise Exception('[!] Error when parsing command line arguments')

    try:
        thes_entries = thes_term(thes_args.term_word, thes_args.antonym)
    except Exception as e:
        print e
        raise Exception('[!] Error occurs when running thes_dump with term_word: {}'.format(thes_args.term_word))

    # Print out the results
    # print '\n' # create some space from command prompt
    for entry in thes_entries:
        print entry
