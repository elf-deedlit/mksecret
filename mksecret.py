#!/usr/bin/env python
# vim:set fileencoding=utf-8 ts=4 sw=4 et:

# 乱数を用いて秘密の文字列用ひらがな文字列を作成する
import argparse
import os
import random
try:
    import secrets
    choice_func = secrets.choice
except ImportError:
    import random
    choice_func = random.choice

def parse_option():
    parser = argparse.ArgumentParser(description = u'ひらがな乱数文字列作成')
    parser.add_argument('--nouseoldkana', action = 'store_true', default = False,
            help = u'「ゐゑ」使わない')
    parser.add_argument('num', type = int, nargs = 1, help = u'文字数')
    return parser.parse_args()

def main():
    options = parse_option()
    num = options.num[0]
    if num < 1:
        num = 8

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
    if not options.nouseoldkana:
        s += u'ゐゑ'

    l = list(s)
    passwd = [choice_func(l) for n in range(0, num)]
    random.shuffle(passwd)
    print(u''.join(passwd))

if __name__=='__main__':
    main()

