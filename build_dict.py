# -*- coding: utf-8 -*-
"""
Created on Thu March 24 16:14:25 2019

@author: yanjun zhou
"""
#sentiDictionay类用于构造情感词典

import thulac

class sentiDictionary:
    def __init__(self):
        pass

    #读取文件中的内容
    def readWords(self,filePath):
        wordlist=[]
        with open(filePath,encoding='utf8') as f:
            for word in f.readlines():
                wordlist.append(word.strip('\n'))
        return wordlist

    #构建程度副词情感词典
    def buildSentiDic(self,levelFile='level_adv.txt'):
        levelWords_utf8=self.readWords(levelFile)
        levelWords_unicode = []
        for word_utf8 in levelWords_utf8:
            levelWords_unicode.append(word_utf8)
        level1_unicode = levelWords_unicode[1:70]       #absolute 69
        level2_unicode = levelWords_unicode[71:113]     #higher 42
        level3_unicode = levelWords_unicode[114:151]    #high 37
        level4_unicode = levelWords_unicode[152:181]    #neutral 29
        level5_unicode = levelWords_unicode[182:195]    #approximate 12
        level6_unicode = levelWords_unicode[196:]       #deny 30
        level_unicode = (level1_unicode,level2_unicode,level3_unicode,level4_unicode,level5_unicode,level6_unicode)
        self.levelWords_unicode = level_unicode
        return level_unicode

    #构建形容词正向词典
    def buildPosadjDict(self,positiveFile='positive.txt'):
        posWords_utf8=self.readWords(positiveFile)
        posWords_unicode=[]
        for word_utf8 in posWords_utf8:
            posWords_unicode.append(word_utf8)
        return posWords_unicode[1:]
    
    #构建形容词负向词典
    def buildNegadjDict(self,negativeFile='negative.txt'):
        negWords_utf8=self.readWords(negativeFile)
        negWords_unicode=[]
        for word_utf8 in negWords_utf8:
            negWords_unicode.append(word_utf8)
        return negWords_unicode[1:]

    #构建动词的情感词典
    def buildSentiverbDic(self,levelFile='level_verb.txt'):
        levelWords_utf8=self.readWords(levelFile)
        levelWords_unicode = []
        for word_utf8 in levelWords_utf8:
            levelWords_unicode.append(word_utf8)
        level1_unicode = levelWords_unicode[1:11]         #积极肯定的动词
        level2_unicode = levelWords_unicode[12:19]        #中性动词
        level3_unicode = levelWords_unicode[20:]         #消极否定的动词
        level_unicode = (level1_unicode,level2_unicode,level3_unicode)
        self.levelWords_unicode = level_unicode
        return level_unicode
