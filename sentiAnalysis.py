# -*- coding: utf-8 -*-
"""
Created on Thu April 25 17:25:30 2019

@author: yanjun zhou
"""

import word_fetch as wf
import avac_score as avac

class senti_AVAC():

    def __init__(self):
        pass

    def sent_sc(self,text):
        word_f = wf.word_classify(text)
        avc = word_f.adv_v_classify()
        aac = word_f.adv_adj_classify()
        if avc != [] and aac == []:
            count = 0
            total_sc = 0
            sc = avac.avac_sc()
            for av in avc:
                print(av)
            for av in avc:
                count += 1
                total_sc += sc.avc_sc(av)
            return total_sc/count
        elif avc == [] and aac != []:
            count = 0
            total_sc = 0
            sc = avac.avac_sc()
            for aa in aac:
                print(aa)
            for aa in avc:
                count += 1
                total_sc += sc.avc_sc(aa)
            return total_sc/count
        elif avc != [] and aac != []:
            sc = avac.avac_sc()
            return (sc.avc_sc(word_f.adv_v_classify())+sc.aac_sc(word_f.adv_adj_classify()))/2
