# -*- coding: utf-8 -*- 
import sys
import argparse

args = sys.argv

parser = argparse.ArgumentParser(description='Read HIRAGANA or KATAKANA Input file and return different KANA')
parser.add_argument('input_file', nargs=1, help='Need Input file name')
parser.add_argument('number', type=int)
args2=parser.parse_args()
#parser.print_help()


if args[1]:
    lines = [line.strip().split('\t') for line in open(args[1], "r")]
for line in lines:
    # number of colum you want to convert
    text = line[args2.number].decode('utf-8')
    d = dict([(x, unichr(x - 0x60)) for x in xrange(ord(u'ァ'), ord(u'ヴ')+1)] + [(x - 0x60, unichr(x)) for x in xrange(ord(u'ァ'), ord(u'ヴ')+1)])
    print text.translate(d)