# This Python file uses the following encoding: utf-8

import numpy as np

class Personality:

    def __init__(self):
        self.pesonality={'ESTP':0,'ISTP':1,'ESFP':2,
                         'ISFP':3,'ESTJ':4,'ISTJ':5,
                         'ESFJ':6,'ISFJ':7,'ENFP':8,
                         'INFP':9,'ENFJ':10,'INFJ':11,
                         'ENTP':12,'INTP':13,'ENTJ':14,'INTJ':15}
        self.matching_matrix=np.zeros((16,16))
        probabilitys={'ESTP':4.3,'ISTP':5.4,'ESFP':8.5,
                      'ISFP':8.8,'ESTJ':8.7,'ISTJ':11.6,
                      'ESFJ':12,'ISFJ':13.8,'ENFP':8.1,
                      'INFP':4.4,'ENFJ':2.5,'INFJ':1.5,
                      'ENTP':3.2,'INTP':3.3,'ENTJ':1.8,	'INTJ':2.1}
        self.ComP={}
        self.InATeam=[]
