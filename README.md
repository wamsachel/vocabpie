# vocabpie: CLI utilties that will look up word definitions, synonyms/antonyms, and etymologies. 
[vocabpie](https://github.com/wamsachel/vocabpie.git) CLI utilties that will look up word definitions, synonyms/antonyms, and etymologies.

> vocabpie is built with [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/#Download) and [requests](http://docs.python-requests.org/en/latest/user/install/#install) 

-----

## Features

+ [x] Console interface
+ [x] Look up word definitions from dictionary.com with the dict utility
+ [x] Look up words from thesaurus.com with the thes utility
+ [x] Look up word etymologies from etymonline.com with the etym utility


## Quickstart

```bash
# look up dictionary definition of the word 'lexicography'
dict lexicography

# look up thesaurus synonyms for the word 'glib'
thes glib

# look up thesaurus antonyms for the word 'glib'
thes -a glib
thes --antonym glib 

# look up etymology for the word 'linguist'
etym linguist

```

## Installation

### Dependencies

+ `[Linux, OSX, Windows]` [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/#Download) and [requests](http://docs.python-requests.org/en/latest/user/install/#install) 

### Development version

The **latest development version** can be installed directly from GitHub:

[vocabpie](https://github.com/wamsachel/vocabpie.git)


## Contributing

Feel free to comment, open a bug report or ask for new features on vocabpie [issues](https://github.com/wamsachel/vocabpie/issues)

If you want to contributing with code:

- Make sure to add tests (do as I say not as I do :p)
- Create a pull request


## License ([MIT License](http://choosealicense.com/licenses/mit/))

The MIT License (MIT)

Copyright (c) 2014-2015 Marc Webbie, <http://github.com/marcwebbie>

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
