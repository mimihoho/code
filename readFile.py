# coding: utf-8

import sys
import argparse #For generating user friendly command line tips
import re
import jaconv # For converting japanese scripts

# string clean up ----------------------------
# Convert target item 1)No Space 2)No Nakaten 3)No Hankaku Katakana
def str_cleanUp(st):
    st = st.replace(" ","")
    st = st.replace("・","")
    st = st.replace("&","アンド")
    st = jaconv.h2z(st, kana=True)
    st = jaconv.hira2kata(st)
    return st
#---------------------------------------------

# Command line help 
args = sys.argv
#print(args)
#print('第１引数：Input file' + args[1])
#print('第２引数：Output file' + args[2])
#print('第３引数：' + args[3])
parser = argparse.ArgumentParser(description='Read from Input file and write in Output file')
parser.add_argument('input_file', nargs=1, help='Need Input file name')
parser.add_argument('output_file', nargs=1, help='Need Output file name')
parser.add_argument('index_number', metavar='N', type=int, nargs='*', help='Index number to modify')
parser.print_help()


# 1) Read file from input_file as 2D array 
if args[1]:
    lines = [line.strip().split('\t') for line in open(args[1], "r")]
line_index = int(args[3])
fh = open(args[2], "w")
#---------------------------------------------------------
# ひらがな ^(\xE3\x81[\x81-\xBF]|\xE3\x82[\x80-\x93])+$
# カタカナ ^(\xe3(\x82[\xa1-\xbf]|\x83[\x80-\xb6]|\x83\xbc))+$
# 半角カタカナ ^(\xEF\xBD[\xA1-\xBF]|\xEF\xBE[\x80-\x9F])+$
#---------------------------------------------------------

# 2) Check if target items are in ZENKAKU KATAKANA
regexp = re.compile(r'^(?:\xe3(\x82[\xa1-\xbf]|\x83[\x80-\xb6]|\x83\xbc))*$')
#regexp = re.compile(r'^[ァ-ヴ]*$')

count = 0
countA = 0
for line in lines:
#    print(line[line_index])
    result = regexp.match(line[line_index])
    if result != None : #print("すべてが全角カタカナ")
        continue
    else: #print("すべてが全角カタカナではない")
        if line[line_index] == '-': # Pronounciation unknown
            count = count+1
        elif re.match(r'.*[A-Z]|[a-z]|[0-9].*$',line[line_index]): # Pronounciation in Alphabet 
            countA = countA+1
            print(line[line_index])
        line[line_index] = str_cleanUp(line[line_index])
# 3) Write in out_file
    for elem in line:
        fh.write(elem + '\t')
    fh.write('\n')
print('Number of unknown pronounciation - : ', count)
print('Number of Alphabet : ', countA)
fh.close()

