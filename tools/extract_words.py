#/usr/bin/env python3
#
# Using data from https://wortschatz.uni-leipzig.de/en/download/Georgian
# To generate syllables run:
# python3 extract_words.py  | tail -n 200 > AA
# cat AA | awk '{ print $2 }' |  python3 transliterate.py > BB
# paste AA BB  | awk '{print "\"" $2 "-" $3 ";\"+"}'
#

import os,sys
import itertools
from collections import defaultdict
import pprint
pp = pprint.pprint


slogi = defaultdict(lambda: 0)

def get_slogs(w):
    w=w.replace('ა', 'ა|').replace('ი', 'ი|').replace('ო', 'ო|').replace('უ', 'უ|').replace('ე', 'ე|')
    
    slogs = [i for i in w.split('|') if len(i) > 1]
    return slogs
    
n = 0
for line in open('kat_wikipedia_2021_10K/kat_wikipedia_2021_10K-words.txt'):
    n += 1
    if n > 100000:
        break
    w = line.split()[1]
    print ('line:', line, 'word:', w)
    
    for sl in get_slogs(w):
        #print ('slog:', sl)
        
        slogi[sl] += 1
#pp(slogi)
ss = [(n,s) for s,n in slogi.items() if n > 10 and len (s)==4]
ss.sort(key=lambda x:x[0])
#pp(ss)
for n, s in ss:
    print (n, s)