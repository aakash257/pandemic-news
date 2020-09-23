import re

def create_cleanerDoc(Doc):
    punc = '!"#$%&\'()*+,-/:;=?@[\\]^`{|}~'

    #lowercase all characters
    cleanerDoc = Doc.lower()

    #remove new line/s '\n'
    cleanerDoc = re.sub('\n', '', cleanerDoc)
    #remove digits with decimals
    cleanerDoc = re.sub('[0-9]+\.[0-9]+', '', cleanerDoc)
    #remove 's
    cleanerDoc = re.sub('\'s', '', cleanerDoc)
    #remove dashes
    cleanerDoc = re.sub('[-]+', ' ', cleanerDoc)
    #remove punctuation
    cleanerDoc = ''.join([char for char in cleanerDoc
                        if char not in set(punc)])

    #remove cnn word that appears at the start of every article
    cleanerDoc = re.sub('$cnn', '', cleanerDoc)

    #remove multiple spaces
    cleanerDoc = re.sub('  +', ' ', cleanerDoc)

    #remove digits
    cleanerDoc = re.sub(' [0-9]+ ', ' ', cleanerDoc)

    #remove space at the end of the string
    cleanerDoc = re.sub(' $', '', cleanerDoc)

    #remove unnecessary full stops
    cleanerDoc = re.sub(' \. ', '. ', cleanerDoc)
    cleanerDoc = re.sub(' \.\.\. ', ' ', cleanerDoc)

    #remove multiple full stops
    cleanerDoc = re.sub('([\w]*)( \.+ )([\w]*)', r'\1. \3', cleanerDoc)

    #remove single characters except i
    cleanerDoc = re.sub(' [abcdefghjklmnopqrstuvwxyz] ', ' ', cleanerDoc)

    #remove remaining unnecessary full stops
    cleanerDoc = re.sub('\.', '', cleanerDoc)

    #remove the spaces at the start of the doc
    cleanerDoc = re.sub('$ ', '', cleanerDoc)

    #remove the spaces at the end of the doc
    cleanerDoc = re.sub(' $', '', cleanerDoc)

    return cleanerDoc
