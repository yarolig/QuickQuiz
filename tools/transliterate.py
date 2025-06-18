#/usr/bin/env python3

import os,sys
import pprint
pp = pprint.pprint


data = (
"ა-А;"+
"ბ-Б;"+
"გ-Г;"+
"დ-Д;"+
"ე-Э;"+
"ვ-В;"+
"ზ-З;"+
"თ-Т';"+
"ი-И;"+
"კ-К;"+
"ლ-Л;"+
"მ-М;"+
"ნ-Н;"+
"ო-О;"+
"პ-П;"+
"ჟ-Ж;"+
"რ-Р;"+
"ს-С;"+
"ტ-Т!;"+
"უ-У;"+
"ფ-П';"+
"ქ-К';"+
"ღ-Г!;"+
"ყ-К!;"+
"შ-Ш;"+
"ჩ-Ч;"+
"ც-Ц;"+
"ძ-Дз;"+
"წ-Ц!;"+
"ჭ-Ч!;"+
"ხ-Х;"+
"ჯ-Дж;"+
"ჰ-Х'")

rep = {}
for rec in data.split(';'):
    k,v = rec.split('-')
    rep [k]=v
#pp(rep)


for line in sys.stdin:
    for k,v in rep.items():
        line = line.replace(k,v)
    sys.stdout.write(line)