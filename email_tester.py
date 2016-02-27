import sys
from imperative_detector import is_imperative
from nltk.tokenize import sent_tokenize
import re

def read_emails(email_name):
    email = open(email_name, 'rb').read()
    email = email.replace('\n', '')
    #email = email.split('.')
    email = re.split('[.?!](?!\d)', email)
    #email = sent_tokenize(email)
    #print email
    for line in email:
        print str(is_imperative(line, verbose = False)) + ' | ' + line

read_emails(sys.argv[1])
