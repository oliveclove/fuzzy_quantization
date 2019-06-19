# -*- coding: utf-8 -*-
"""
Created on Thu April 23 20:03:30 2019

@author: yanjun zhou
"""
import word_fetch as wf
import mmtd_quantizatin as mq
import build_dict as bd

#两种AVAC的得分计算方法
class avac_sc():
    
    def __init__(self):
        pass
    
    #基于MMTD的AVC得分规则(0~1.5之间)，判断词组的价值偏向
    def avc_sc(self, avc):
        sentidic = bd.sentiDictionary()
        level_verb = sentidic.buildSentiverbDic()
        mmtd = mq.mmtd_quantify(0.05,0.95)
        adv_sc = 0.0
        if mmtd.DistanceT(avc[0]) > mmtd.DistanceF(avc[0]):       #表示强化了观点
            adv_sc = mmtd.DistanceT(avc[0])
        elif mmtd.DistanceT(avc[0]) < mmtd.DistanceF(avc[0]):     #表示弱化了观点
            adv_sc = mmtd.DistanceT(avc[0])                        
        v_sc = 0.0
        if avc[1] in level_verb[0]:
            v_sc = 0.5
        elif avc[1] in level_verb[1]:
            v_sc = 1
        else:
            v_sc = 1.5
        return adv_sc * v_sc
        
    #基于MMTD的AAC得分规则(0~1之间)，强化程度分析
    def aac_sc(self,aac):
        sentidic = bd.sentiDictionary()
        positive = sentidic.buildPosadjDict()
        negtive = sentidic.buildNegadjDict()
        mmtd = mq.mmtd_quantify(0.05,0.95)
        adv_sc = 0.0
        if mmtd.DistanceT(aac[0]) > mmtd.DistanceF(aac[0]):       #表示强化了观点
            adv_sc = mmtd.DistanceT(aac[0])
        elif mmtd.DistanceT(aac[0]) < mmtd.DistanceF(aac[0]):     #表示弱化了观点
            adv_sc = mmtd.DistanceT(aac[0])
        adj_sc = 0.0
        if aac[1] in positive:
            adj_sc = 1.5
        elif aac[1] in negtive:
            adj_sc = 0.5
        else:
            adj_sc = 1
        return adj_sc * adv_sc
        
    
