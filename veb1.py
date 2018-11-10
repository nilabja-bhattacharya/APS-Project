import sys
import math
import time 
import random
from collections import defaultdict

BASE = 2

class vEBLeaf(object):
    def __init__(self, word_size):
        self.word_size = word_size
        self.values = [False, False]

    def min(self):
        for i in range(2):
            if self.values[i]:
                return i
        return None
    
    def max(self):
        for i in range(1, -1, -1):
            if self.values[i]:
                return i
        return None

    def insert(self, x):
        self.values[x] = True

    def delete(self, x):
        self.values[x]= False

class vEBTree(object):
    def __init__(self, word_size):
        self.min_ = self.max_ = None
        self.word_size =  word_size
        self.summary_size = int(self.word_size/2)
        self.u = 1<<self.summary_size
        self.cluster = [None]*(self.u)
        self.mask = self.u - 1
        self.summary = vEB.of_size(self.summary_size)

    def __contains__(self,x):
        if self.min() is None:
            return False
        elif self.min() == x:
            return True
        else:
            high = self.high(x)
            low = self.low(x)
            if self.cluster[high] is None:
                return False
            else:
                return low in self.cluster[high]

    def high(self, x):
        return x>>int(self.summary_size)

    def low(self, x):
        return x&(self.mask)
    def index(self, i, j):
        return (i<<self.summary_size) | j

    def insert(self, x):
        if self.min() is None:
            self.min_ = self.max_ = x
            return
        if x == self.min():
            return
        if x<self.min():
            self.min_, x = x, self.min_
        if x>self.max():
            self.max_ = x

        cluster_index = x>>int(self.summary_size)
        element_index = x&(self.mask)
#         clustr = self.cluster[cluster_index]
        if self.cluster[cluster_index] is None:
             self.cluster[cluster_index] = vEB.of_size(self.summary_size)

        if self.cluster[cluster_index].min() is None:
            self.summary.insert(cluster_index)

        self.cluster[cluster_index].insert(element_index)

    def max(self):
        return self.max_
    def min(self):
        return self.min_
    
    def delete(self, x):
        if self.min() is None or x<self.min():
            return
            
        if x == self.min():
            if self.summary is None or self.summary.min() is None:
                self.min_ = self.max_ = None
                return
            cluster_index = self.summary.min()
            element_index = self.cluster[cluster_index].min()

            x = self.min_ = (cluster_index<<self.summary_size) | element_index

        cluster_index = x>>int(self.summary_size)
        element_index = x&(self.mask)
#         clustr = self.cluster[cluster_index]

        if self.cluster[cluster_index] is None:
            return 
        self.cluster[cluster_index].delete(element_index)

        if self.cluster[cluster_index].min() is None:
            self.cluster[cluster_index]=None
            self.summary.delete(cluster_index)

        if x==self.max():
            
            if self.summary.max() is None:
                self.max_ = self.min()
            else:
                cluster_index = self.summary.max()
                element_index = self.cluster[cluster_index].max()
                self.max_ = (cluster_index<<self.summary_size) | element_index

class vEB(object):
    @classmethod
    def of_size(cls, word_size):
        return vEBLeaf(word_size) if word_size<BASE else vEBTree(word_size)
