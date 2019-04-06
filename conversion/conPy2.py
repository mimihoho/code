# -*- coding: utf-8 -*- 
import sys
import argparse

args = sys.argv
"""
parser = argparse.ArgumentParser(description='Read HIRAGANA or KATAKANA Input file and return different KANA')
parser.add_argument('input_file', nargs=1, help='Need Input file name')
parser.print_help()
"""

if args[1]:
    lines = [line.strip().split('\t') for line in open(args[1], "r")]
for line in lines:
    # number of colum you want to convert
    text = line[1].decode('utf-8')
    #for item in text:
    #text = u'ドラえもん 新・のび太の大魔境 あっぷる'
    d = dict([(x, unichr(x - 0x60)) for x in xrange(ord(u'ァ'), ord(u'ヴ')+1)] + [(x - 0x60, unichr(x)) for x in xrange(ord(u'ァ'), ord(u'ヴ')+1)])
    print text.translate(d)