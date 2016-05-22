#!/usr/bin/python
# vim:set fileencoding=utf-8 ts=4 sw=4 et:

# 乱数を用いて秘密の文字列用ひらがな文字列を作成する

import os, random
from optparse import OptionParser, make_option

option_list = [
    make_option('-n', '--num', action='store', type='int', dest='num',
        help=u'使用する桁数', default=16),
]

def main():
    parser = OptionParser(usage = u'%prog [options]',
        description = u'乱数生成',
        option_list = option_list)

    (options, args) = parser.parse_args()

    n = options.num
    if n < 1:
        n = 1

    s = u'あいうえお'
    s += u'かきくけこ'
    s += u'さしすせそ'
    s += u'たちつてと'
    s += u'なにぬねの'
    s += u'はひふへほ'
    s += u'まみむめも'
    s += u'やゆよ'
    s += u'らりるれろ'
    s += u'わをん'
    s += u'ゐゑ'

    l = list(s)
    r = []
    for i in xrange(0, n):
        r.append(random.choice(l))
    print u''.join(r)

if __name__=='__main__':
    main()

