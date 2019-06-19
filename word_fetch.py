# -*- coding: utf-8 -*-
"""
Created on Thu March 23 14:48:39 2019

@author: yanjun zhou
"""
import thulac

#word_classify用于词的分类

class word_classify():
    def __init__(self,text):
        self.text=text

    #句子的分词
    def split_sentenence(self):
        thul=thulac.thulac()
        words=thul.cut(self.text)
        wordlist=[word[0] for word in words]
        return wordlist
    
    #副词分类
    def adverb_classify(self):
        thul=thulac.thulac()
        words=thul.cut(self.text)
        adverb=[word[0] for word in words if word[1]=='d']
        return adverb

    #形容词分类
    def adjective_classify(self):
        thul=thulac.thulac()
        words=thul.cut(self.text)
        adjective=[word[0] for word in words if word[1]=='a']
        return adjective

    #动词分类
    def verb_classify(self):
        thul=thulac.thulac()
        words=thul.cut(self.text)
        verb=[word[0] for word in words if word[1]=='v']
        return verb

     #名词分类
    def noun_classify(self):
        thul=thulac.thulac()
        words=thul.cut(self.text)
        noun=[word[0] for word in words if word[1]=='n']
        return noun

    #双连词分类器
    def bigrams(self):
        thul=thulac.thulac()
        words=thul.cut(self.text)
        bigram=[words[i:i+2] for i in range(len(words)-1)]
        return bigram

    #副词动词组合(AVC)
    def adv_v_classify(self):
        bigs=self.bigrams()
        adv_v=[[big[0][0],big[1][0]] for big in bigs if big[0][1]=='d' and big[1][1]=='v']
        return adv_v
        
    #副词形容词组合(AAC)
    def adv_adj_classify(self):
        bigs=self.bigrams()
        adv_adj=[[big[0][0],big[1][0]] for big in bigs if big[0][1]=='d' and big[1][1]=='a']
        return adv_adj

    
        
