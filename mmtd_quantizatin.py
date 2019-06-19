# -*- coding: utf-8 -*-
"""
Created on Thu March 24 16:14:25 2019

@author: oliveclove
"""
import build_dict as bd

#基于MMTD的副词量化模型
class mmtd_quantify:
    
    def __init__(self,ff,ft):
        self.ff=ff
        self.ft=ft

    #计算词相对于褒的距离比率函数
    def DistanceT(self,word):
        sentidic=bd.sentiDictionary()
        level_adv=sentidic.buildSentiDic()
        if word in level_adv[0]:
            return 0.975
        if word in level_adv[1]:
            return (0.8375-self.ff)/(self.ft-self.ff)
        if word in level_adv[2]:
            return (0.6125-self.ff)/(self.ft-self.ff)
        if word in level_adv[3]:
            return (-0.6125-self.ff)/(self.ft-self.ff)
        if word in level_adv[4]:
            return (-0.8375-self.ff)/(self.ft-self.ff)
        if word in level_adv[5]:
            return 0.025

    #计算词相对于贬的距离比率函数
    def DistanceF(self,word):
        sentidic=bd.sentiDictionary()
        level_adv=sentidic.buildSentiDic()
        if word in level_adv[0]:
            return 0.025
        if word in level_adv[1]:
            return (self.ft-0.8375)/(self.ft-self.ff)
        if word in level_adv[2]:
            return (self.ft-0.6125)/(self.ft-self.ff)
        if word in level_adv[3]:
            return (self.ft+0.6125)/(self.ft-self.ff)
        if word in level_adv[4]:
            return (self.ft+0.8375)/(self.ft-self.ff)
        if word in level_adv[5]:
            return 0.975
