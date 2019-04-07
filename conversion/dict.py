#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys
import argparse #For generating user friendly command line tips

"""かな⇔ローマ字を変換する"""

def _make_kana_convertor():
    """ひらがな⇔カタカナ変換器を作る"""
    kata = {
        'ア':'あ', 'イ':'い', 'ウ':'う', 'エ':'え', 'オ':'お',
        'カ':'か', 'キ':'き', 'ク':'く', 'ケ':'け', 'コ':'こ',
        'サ':'さ', 'シ':'し', 'ス':'す', 'セ':'せ', 'ソ':'そ',
        'タ':'た', 'チ':'ち', 'ツ':'つ', 'テ':'て', 'ト':'と',
        'ナ':'な', 'ニ':'に', 'ヌ':'ぬ', 'ネ':'ね', 'ノ':'の',
        'ハ':'は', 'ヒ':'ひ', 'フ':'ふ', 'ヘ':'へ', 'ホ':'ほ',
        'マ':'ま', 'ミ':'み', 'ム':'む', 'メ':'め', 'モ':'も',
        'ヤ':'や', 'ユ':'ゆ', 'ヨ':'よ', 'ラ':'ら', 'リ':'り',
        'ル':'る', 'レ':'れ', 'ロ':'ろ', 'ワ':'わ', 'ヲ':'を',
        'ン':'ん',
        
        'ガ':'が', 'ギ':'ぎ', 'グ':'ぐ', 'ゲ':'げ', 'ゴ':'ご',
        'ザ':'ざ', 'ジ':'じ', 'ズ':'ず', 'ゼ':'ぜ', 'ゾ':'ぞ',
        'ダ':'だ', 'ヂ':'ぢ', 'ヅ':'づ', 'デ':'で', 'ド':'ど',
        'バ':'ば', 'ビ':'び', 'ブ':'ぶ', 'ベ':'べ', 'ボ':'ぼ',
        'パ':'ぱ', 'ピ':'ぴ', 'プ':'ぷ', 'ペ':'ぺ', 'ポ':'ぽ',
        
        'ァ':'ぁ', 'ィ':'ぃ', 'ゥ':'ぅ', 'ェ':'ぇ', 'ォ':'ぉ',
        'ャ':'ゃ', 'ュ':'ゅ', 'ョ':'ょ',
        'ヴ':'&#12436;', 'ッ':'っ', 'ヰ':'ゐ', 'ヱ':'ゑ',
        }
    
    # ひらがな → カタカナ のディクショナリをつくる
    hira = dict([(v, k) for k, v in kata.items() ])
    
    re_hira2kata = re.compile("|".join(map(re.escape, hira)))
    re_kata2hira = re.compile("|".join(map(re.escape, kata)))
    
    def _hiragana2katakana(text):
        return re_hira2kata.sub(lambda x: hira[x.group(0)], text)
    
    def _katakana2hiragana(text):
        return re_kata2hira.sub(lambda x: kata[x.group(0)], text)
    
    return (_hiragana2katakana, _katakana2hiragana)


hiragana2katakana, katakana2hiragana = _make_kana_convertor()

################################################################################

def _make_romaji_convertor():
    """ローマ字⇔かな変換器を作る"""
    master = {
        'a'  :'ア', 'i'  :'イ', 'u'  :'ウ', 'e'  :'エ', 'o'  :'オ',
        'ka' :'カ', 'ki' :'キ', 'ku' :'ク', 'ke' :'ケ', 'ko' :'コ',
        'sa' :'サ', 'shi':'シ', 'su' :'ス', 'se' :'セ', 'so' :'ソ',
        'ta' :'タ', 'chi':'チ', 'tu' :'ツ', 'te' :'テ', 'to' :'ト',
        'na' :'ナ', 'ni' :'ニ', 'nu' :'ヌ', 'ne' :'ネ', 'no' :'ノ',
        'ha' :'ハ', 'hi' :'ヒ', 'fu' :'フ', 'he' :'ヘ', 'ho' :'ホ',
        'ma' :'マ', 'mi' :'ミ', 'mu' :'ム', 'me' :'メ', 'mo' :'モ',
        'ya' :'ヤ', 'yu' :'ユ', 'yo' :'ヨ',
        'ra' :'ラ', 'ri' :'リ', 'ru' :'ル', 're' :'レ', 'ro' :'ロ',
        'wa' :'ワ', 'wo' :'ヲ', 'n'  :'ン', 'vu' :'ヴ',
        'ga' :'ガ', 'gi' :'ギ', 'gu' :'グ', 'ge' :'ゲ', 'go' :'ゴ',
        'za' :'ザ', 'ji' :'ジ', 'zu' :'ズ', 'ze' :'ゼ', 'zo' :'ゾ',
        'da' :'ダ', 'di' :'ヂ', 'du' :'ヅ', 'de' :'デ', 'do' :'ド',
        'ba' :'バ', 'bi' :'ビ', 'bu' :'ブ', 'be' :'ベ', 'bo' :'ボ',
        'pa' :'パ', 'pi' :'ピ', 'pu' :'プ', 'pe' :'ペ', 'po' :'ポ',
        
        'kya':'キャ', 'kyi':'キィ', 'kyu':'キュ', 'kye':'キェ', 'kyo':'キョ',
        'gya':'ギャ', 'gyi':'ギィ', 'gyu':'ギュ', 'gye':'ギェ', 'gyo':'ギョ',
        'sha':'シャ',               'shu':'シュ', 'she':'シェ', 'sho':'ショ',
        'ja' :'ジャ',               'ju' :'ジュ', 'je' :'ジェ', 'jo' :'ジョ',
        'cha':'チャ',               'chu':'チュ', 'che':'チェ', 'cho':'チョ',
        'dya':'ヂャ', 'dyi':'ヂィ', 'dyu':'ヂュ', 'dhe':'デェ', 'dyo':'ヂョ',
        'nya':'ニャ', 'nyi':'ニィ', 'nyu':'ニュ', 'nye':'ニェ', 'nyo':'ニョ',
        'hya':'ヒャ', 'hyi':'ヒィ', 'hyu':'ヒュ', 'hye':'ヒェ', 'hyo':'ヒョ',
        'bya':'ビャ', 'byi':'ビィ', 'byu':'ビュ', 'bye':'ビェ', 'byo':'ビョ',
        'pya':'ピャ', 'pyi':'ピィ', 'pyu':'ピュ', 'pye':'ピェ', 'pyo':'ピョ',
        'mya':'ミャ', 'myi':'ミィ', 'myu':'ミュ', 'mye':'ミェ', 'myo':'ミョ',
        'rya':'リャ', 'ryi':'リィ', 'ryu':'リュ', 'rye':'リェ', 'ryo':'リョ',
        'fa' :'ファ', 'fi' :'フィ',               'fe' :'フェ', 'fo' :'フォ',
        'wi' :'ウィ', 'we' :'ウェ', 
        'va' :'ヴァ', 'vi' :'ヴィ', 've' :'ヴェ', 'vo' :'ヴォ',
        
        'kwa':'クァ', 'kwi':'クィ', 'kwu':'クゥ', 'kwe':'クェ', 'kwo':'クォ',
        'kha':'クァ', 'khi':'クィ', 'khu':'クゥ', 'khe':'クェ', 'kho':'クォ',
        'gwa':'グァ', 'gwi':'グィ', 'gwu':'グゥ', 'gwe':'グェ', 'gwo':'グォ',
        'gha':'グァ', 'ghi':'グィ', 'ghu':'グゥ', 'ghe':'グェ', 'gho':'グォ',
        'swa':'スァ', 'swi':'スィ', 'swu':'スゥ', 'swe':'スェ', 'swo':'スォ',
        'swa':'スァ', 'swi':'スィ', 'swu':'スゥ', 'swe':'スェ', 'swo':'スォ',
        'zwa':'ズヮ', 'zwi':'ズィ', 'zwu':'ズゥ', 'zwe':'ズェ', 'zwo':'ズォ',
        'twa':'トァ', 'twi':'トィ', 'twu':'トゥ', 'twe':'トェ', 'two':'トォ',
        'dwa':'ドァ', 'dwi':'ドィ', 'dwu':'ドゥ', 'dwe':'ドェ', 'dwo':'ドォ',
        'mwa':'ムヮ', 'mwi':'ムィ', 'mwu':'ムゥ', 'mwe':'ムェ', 'mwo':'ムォ',
        'bwa':'ビヮ', 'bwi':'ビィ', 'bwu':'ビゥ', 'bwe':'ビェ', 'bwo':'ビォ',
        'pwa':'プヮ', 'pwi':'プィ', 'pwu':'プゥ', 'pwe':'プェ', 'pwo':'プォ',
        'phi':'プィ', 'phu':'プゥ', 'phe':'プェ', 'pho':'フォ',
        }
    
    
    romaji_asist = {
        'si' :'シ'  , 'ti' :'チ'  , 'hu' :'フ' , 'zi':'ジ',
        'sya':'シャ', 'syu':'シュ', 'syo':'ショ',
        'tya':'チャ', 'tyu':'チュ', 'tyo':'チョ',
        'cya':'チャ', 'cyu':'チュ', 'cyo':'チョ',
        'jya':'ジャ', 'jyu':'ジュ', 'jyo':'ジョ', 'pha':'ファ', 
        'qa' :'クァ', 'qi' :'クィ', 'qu' :'クゥ', 'qe' :'クェ', 'qo':'クォ',
        
        'ca' :'カ', 'ci':'シ', 'cu':'ク', 'ce':'セ', 'co':'コ',
        'la' :'ラ', 'li':'リ', 'lu':'ル', 'le':'レ', 'lo':'ロ',

        'mb' :'ム', 'py':'パイ', 'tho': 'ソ', 'thy':'ティ', 'oh':'オウ',
        'by':'ビィ', 'cy':'シィ', 'dy':'ディ', 'fy':'フィ', 'gy':'ジィ',
        'hy':'シー', 'ly':'リィ', 'ny':'ニィ', 'my':'ミィ', 'ry':'リィ',
        'ty':'ティ', 'vy':'ヴィ', 'zy':'ジィ',
        
        'b':'ブ', 'c':'ク', 'd':'ド', 'f':'フ'  , 'g':'グ', 'h':'フ', 'j':'ジ',
        'k':'ク', 'l':'ル', 'm':'ム', 'p':'プ'  , 'q':'ク', 'r':'ル', 's':'ス',
        't':'ト', 'v':'ヴ', 'w':'ゥ', 'x':'クス', 'y':'ィ', 'z':'ズ',
        }
    

    kana_asist = { 'a':'ァ', 'i':'ィ', 'u':'ゥ', 'e':'ェ', 'o':'ォ', }
    
    
    def __romaji2kana():
        romaji_dict = {}
        for tbl in master, romaji_asist:
            for k, v in tbl.items(): romaji_dict[k] = v
        
        romaji_keys = romaji_dict.keys()
        romaji_keys.sort(key=lambda x:len(x), reverse=True)
        
        re_roma2kana = re.compile("|".join(map(re.escape, romaji_keys)))
        # m の後ろにバ行、パ行のときは "ン" と変換
        rx_mba = re.compile("m(b|p)([aiueo])")
        # 子音が続く時は "ッ" と変換
        rx_xtu = re.compile(r"([bcdfghjklmpqrstvwxyz])\1")
        # 母音が続く時は "ー" と変換
        rx_a__ = re.compile(r"([aiueo])\1")
        
        def _romaji2katakana(text):
            result = text.lower()
            result = rx_mba.sub(r"ン\1\2", result)
            result = rx_xtu.sub(r"ッ\1"  , result)
            result = rx_a__.sub(r"\1ー"  , result)
            print "_phoneme2katakana result = ", re_roma2kana.sub(lambda x: romaji_dict[x.group(0)], result)
            return re_roma2kana.sub(lambda x: romaji_dict[x.group(0)], result)
        
        def _romaji2hiragana(text):
            result = _romaji2katakana(text)
            print "_phoneme2hiragana result = ", katakana2hiragana(result)
            return katakana2hiragana(result)
        
        return _romaji2katakana, _romaji2hiragana
    
    
    def __kana2romaji():
        kana_dict = {}
        for tbl in master, kana_asist:
            for k, v in tbl.items(): kana_dict[v] = k

        kana_keys = kana_dict.keys()
        kana_keys.sort(key=lambda x:len(x), reverse=True)
        
        re_kana2roma = re.compile("|".join(map(re.escape, kana_keys)))
        rx_xtu = re.compile("ッ(.)") # 小さい "ッ" は直後の文字を２回に変換
        rx_ltu = re.compile("ッ$"  ) # 最後の小さい "ッ" は消去(?)
        rx_er  = re.compile("(.)ー") # "ー"は直前の文字を２回に変換
        rx_n   = re.compile(r"n(b|p)([aiueo])") # n の後ろが バ行、パ行 なら m に修正
        rx_oo  = re.compile(r"([aiueo])\1")      # oosaka → osaka
        
        def _kana2romaji(text):
            result = hiragana2katakana(text)
            result = re_kana2roma.sub(lambda x: kana_dict[x.group(0)], result)
            result = rx_xtu.sub(r"\1\1" , result)
            result = rx_ltu.sub(r""     , result)
            result = rx_er.sub (r"\1\1" , result)
            result = rx_n.sub  (r"m\1\2", result)
            result = rx_oo.sub (r"\1"   , result)
            return result
        return _kana2romaji
    
    a, b = __romaji2kana()
    c    = __kana2romaji()
    
    return  a, b, c


romaji2katakana, romaji2hiragana, kana2romaji = _make_romaji_convertor()

################################################################################

def _make_phoneme_convertor():
    #Phoneme⇔かな変換器を作る
    phoneme_master = {
        'A'  :'ア', 'I'  :'イ', 'U'  :'ウ', 'E'  :'エ', 'O'  :'オ',
        'KA' :'カ', 'KI' :'キ', 'KU' :'ク', 'KE' :'ケ', 'KO' :'コ',
        'SA' :'サ', 'SHI':'シ', 'SU' :'ス', 'SE' :'セ', 'SO' :'ソ',
        'TA' :'タ', 'CHI':'チ', 'TSU' :'ツ', 'TE' :'テ', 'TO' :'ト',
        'NA' :'ナ', 'NI' :'ニ', 'NU' :'ヌ', 'NE' :'ネ', 'NO' :'ノ',
        'HA' :'ハ', 'HI' :'ヒ', 'FU' :'フ', 'HE' :'ヘ', 'HO' :'ホ',
        'MA' :'マ', 'MI' :'ミ', 'MU' :'ム', 'ME' :'メ', 'MO' :'モ',
        'YA' :'ヤ', 'YU' :'ユ', 'YO' :'ヨ',
        'RA' :'ラ', 'RI' :'リ', 'RU' :'ル', 'RE' :'レ', 'RO' :'ロ',
        'WA' :'ワ', 'WO' :'ヲ', 'NG'  :'ン', 'VU' :'ヴ',
        'GA' :'ガ', 'GI' :'ギ', 'GU' :'グ', 'GE' :'ゲ', 'GO' :'ゴ',
        'ZA' :'ザ', 'JI' :'ジ', 'ZU' :'ズ', 'ZE' :'ゼ', 'ZO' :'ゾ',
        'DA' :'ダ', 'DI' :'ディ', 'DU' :'ドゥ', 'DE' :'デ', 'DO' :'ド',
        'BA' :'バ', 'BI' :'ビ', 'BU' :'ブ', 'BE' :'ベ', 'BO' :'ボ',
        'PA' :'パ', 'PI' :'ピ', 'PU' :'プ', 'PE' :'ペ', 'PO' :'ポ',
        
        'KYA':'キャ', 'KYI':'キィ', 'KYU':'キュ', 'KYE':'キェ', 'KYO':'キョ',
        'GYA':'ギャ', 'GYI':'ギィ', 'GYU':'ギュ', 'GYE':'ギェ', 'GYO':'ギョ',
        'SHA':'シャ',               'SHU':'シュ', 'SHE':'シェ', 'SHO':'ショ',
        'JA' :'ジャ',               'JU' :'ジュ', 'JE' :'ジェ', 'JO' :'ジョ',
        'TI' :'ティ',
        'CHA':'チャ',               'CHU':'チュ', 'CHE':'チェ', 'CHO':'チョ',
        'NYA':'ニャ', 'NYI':'ニィ', 'NYU':'ニュ', 'NYE':'ニェ', 'NYO':'ニョ',
        'HYA':'ヒャ', 'HYI':'ヒィ', 'HYU':'ヒュ', 'HYE':'ヒェ', 'HYO':'ヒョ',
        'BYA':'ビャ', 'BYI':'ビィ', 'BYU':'ビュ', 'BYE':'ビェ', 'BYO':'ビョ',
        'PYA':'ピャ', 'PYI':'ピィ', 'PYU':'ピュ', 'PYE':'ピェ', 'PYO':'ピョ',
        'MYA':'ミャ', 'MYI':'ミィ', 'MYU':'ミュ', 'MYE':'ミェ', 'MYO':'ミョ',
        'RYA':'リャ', 'RYI':'リィ', 'RYU':'リュ', 'RYE':'リェ', 'RYO':'リョ',
        'FA' :'ファ', 'FI' :'フィ',               'FE' :'フェ', 'FO' :'フォ',
        'WI' :'ウィ', 'WE' :'ウェ', 
        
        'KWA':'クァ', 'KWI':'クィ', 'KWU':'クゥ', 'KWE':'クェ', 'KWO':'クォ',
        'KHA':'クァ', 'KHI':'クィ', 'KHU':'クゥ', 'KHE':'クェ', 'KHO':'クォ',
        'GWA':'グァ', 'GWI':'グィ', 'GWU':'グゥ', 'GWE':'グェ', 'GWO':'グォ',
        'GHA':'グァ', 'GHI':'グィ', 'GHU':'グゥ', 'GHE':'グェ', 'GHO':'グォ', 
        'Q':'ッ'
        }

    phoneme_kana_asist = { 'AA':'アー', 'II':'イー', 'UU':'ウー', 'EE':'エー', 'OO':'オー', }

    def __phoneme2kana():
        phoneme_dict = {}
        for tbl in phoneme_master, phoneme_kana_asist:
            for k, v in tbl.items(): 
                phoneme_dict[k] = v
        
        phoneme_keys = phoneme_dict.keys()
        phoneme_keys.sort(key=lambda x:len(x), reverse=True)
        
        re_phone2kana = re.compile("|".join(map(re.escape, phoneme_keys)))
        # m の後ろにバ行、パ行のときは "ン" と変換
        rx_mba = re.compile("M(B|P)([AIUEO])")
        # 子音が続く時は "ッ" と変換
        #rx_xtu = re.compile(r"([bcdfghjklmpqrstvwxyz])\1")
        # 母音が続く時は "ー" と変換
        rx_a__ = re.compile(r"([AIUEO])\1")
        
        def _phoneme2katakana(text):
            result = text.upper()
            result = rx_mba.sub(r"ン\1\2", result)
            #result = rx_xtu.sub(r"ッ\1"  , result)
            result = rx_a__.sub(r"\1ー"  , result)
            #print "_phoneme2katakana result = ", re_phone2kana.sub(lambda x: phoneme_dict[x.group(0)], result)
            return re_phone2kana.sub(lambda x: phoneme_dict[x.group(0)], result)
        
        def _phoneme2hiragana(text):
            result = _phoneme2katakana(text)
            #print "_phoneme2hiragana result = ", katakana2hiragana(result)
            return katakana2hiragana(result)
       
        return _phoneme2katakana, _phoneme2hiragana


    def __kana2phoneme():
        kana_dict = {}
        for tbl in phoneme_master, phoneme_kana_asist:
            for k, v in tbl.items(): kana_dict[v] = k

        kana_keys = kana_dict.keys()
        kana_keys.sort(key=lambda x:len(x), reverse=True)
        
        re_kana2phon = re.compile("|".join(map(re.escape, kana_keys)))
        #rx_xtu = re.compile("ッ(.)") # 小さい "ッ" は直後の文字を２回に変換
        #rx_ltu = re.compile("ッ$"  ) # 最後の小さい "ッ" は消去(?)
        rx_er  = re.compile("(.)ー") # "ー"は直前の文字を２回に変換
        #rx_n   = re.compile(r"n(b|p)([aiueo])") # n の後ろが バ行、パ行 なら m に修正
        #rx_oo  = re.compile(r"([aiueo])\1")      # oosaka → osaka
        
        def _kana2phoneme(text):
            result = hiragana2katakana(text)
            result = re_kana2phon.sub(lambda x: kana_dict[x.group(0)], result)
            #result = rx_xtu.sub(r"\1\1" , result)
            #result = rx_ltu.sub(r""     , result)
            result = rx_er.sub (r"\1\1" , result)
            #result = rx_n.sub  (r"m\1\2", result)
            #result = rx_oo.sub (r"\1"   , result)
            return result
        return _kana2phoneme
    
    a, b = __phoneme2kana()
    c    = __kana2phoneme()
    
    return  a, b, c


phoneme2katakana, phoneme2hiragana, kana2phoneme = _make_phoneme_convertor()

################################################################################

def _make_number_convertor():
    """Number⇔漢字number変換器を作る"""
    num = {
        '1':'一', '2':'二', '3':'三', '4':'四', '5':'五',
        '6':'六', '7':'七', '8':'八', '9':'九', '0':'零'
        }
    numKata = {
        '1':'イチ', '2':'ニ', '3':'サン', '4':'ヨン', '5':'ゴ',
        '6':'ロク', '7':'シチ', '8':'ハチ', '9':'キュー', '0':'ゼロ'
        }
    katakana_number = {
        'イチ':'一', 'ニ':'二', 'サン':'三', 'ヨン':'四', 'ゴ':'五',
        'ロク':'六', 'ナナ':'七', 'ハチ':'八', 'キュー':'九', 'ジュー':'零'
    }
    katakana_number = {
        'イチ':'一', 'ニ':'二', 'サン':'三', 'ヨン':'四', 'ゴ':'五',
        'ロク':'六', 'ナナ':'七', 'ハチ':'八', 'キュー':'九', 'ジュー':'零'
    }
    
    # 数日 → 漢字数字 のディクショナリをつくる
    kan = dict([(v, k) for k, v in num.items() ])
    
    re_num2kan = re.compile("|".join(map(re.escape, num)))
    re_kan2num = re.compile("|".join(map(re.escape, kan)))
    
    def _kanji2number(text):
        return re_kan2num.sub(lambda x: kan[x.group(0)], text)
    
    def _number2kanji(text):
        return re_num2kan.sub(lambda x: num[x.group(0)], text)
    
    return (_kanji2number, _number2kanji)


kanji2number, number2kanji = _make_number_convertor()

################################################################################


if __name__ == "__main__":
    args = sys.argv
    parser = argparse.ArgumentParser(description='Read HIRAGANA Input file and return in KATAKANA')
    parser.add_argument('input_file', nargs=1, help='Need Input file name')
    parser.add_argument('mode', type=int)
    parser.add_argument('number', type=int)
    #parser.print_help()
    args2=parser.parse_args()

    MODE = {
        1: 'hiragana2katakana',
        2: 'katakana2hiragana',
        3: 'phoneme2hiragana',
        4: 'phoneme2katakana',
        5: 'kana2phoneme',
        6: 'kana2romaji',
        7: 'number2kanji',
        8: 'kanji2number'
    }
    if args[1]:
        lines = [line.strip().split('\t') for line in open(args[1], "r")]
        for line in lines:
            text = line[args2.number]
            if args2.mode == 1:
                print text, "\t", hiragana2katakana(text)
            elif args2.mode == 2:
                print text, "\t", katakana2hiragana(text)
            elif args2.mode == 3:
                print text, "\t", phoneme2hiragana(text)
            elif args2.mode == 4:
                print text, "\t", phoneme2katakana(text)
            elif args2.mode == 5:
               print text, "\t", kana2phoneme(text)
            elif args2.mode == 6:
                print text, "\t", romaji2katakana(text)  
            elif args2.mode == 7:
                print text, "\t", number2kanji(text)
            elif args2.mode == 8:
                print text, "\t", kanji2number(text)       
            else:
                print "OUT = ", args2.mode

    