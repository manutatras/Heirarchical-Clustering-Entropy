#For clustering attributes
from __future__ import division
import math
import pandas as pd
import numpy as np
import pickle
#from scipy.spatial.distance import pdist
from scipy.cluster import hierarchy

class Attr_group():
    
    
    def boxplot(self,Y):
        #For getting the IQR from box plot and calculation
        Y1 = Y[:,2]
        q75,q25 = np.percentile(Y1, [75,25])
        calc = np.median(Y1)+1.5*(q75-q25)
        for i in range(len(Y1)):
            max_d = Y1[i-1]
            if Y1[i] > calc:
                break

        #Details of the heights of clustering and the height which the cut is calculated
        pickle.dump([Y1,max_d],open("hierarchy_details.pkl","wb"))
        return max_d
        
    def entropy_calc(self,elem):
        #Function for getting entropy
        lns = elem.sum()
        entrpy = -1*sum([(count/lns)*math.log(count/lns,2) for count in elem])
        
        return entrpy

    def dist_entr(self,a,b):
        #For calculating the entropy gain
        entl = self.entropy_calc(a)
        entr = self.entropy_calc(b)

        elem = np.array([a[ii]+b[ii] for ii in xrange(len(b))])
        el_sum = elem.sum()

        #Old entropy.... Calculating individual entropy
        old_entr = self.entropy_calc(elem)
        
        #New entropy.... Calculating entropy based on its children
        new_entr = (a.sum()/el_sum)*entl+(b.sum()/el_sum)*entr
        
        #Calculating entropy gain or information loss
        entrpy_gain = old_entr-new_entr

        return entrpy_gain

    
    def attr_clustering(self,X,label_in,a):
        #For doing hierarchical clustering
        #generate the linkage matrix
        Z = hierarchy.linkage(X, method='complete',metric = self.dist_entr)

        #Variable used for creating dendrogram
        pickle.dump(Z,open("hierarchy_Z.pkl","wb"))
       
        #Code for calculating the number of clusters
        #Here the code will return the max_depth which the information loss is higher than its children
        max_d = self.boxplot(Z)
        
        #Flattening the clusters based on distance
        cls = hierarchy.fcluster(Z,max_d, criterion='distance')
        clusters = np.array([str(i) for i in cls])
        
        #Dataframe containing entries and corresponding clusters
        df1 = pd.DataFrame({a+"_cid":clusters,a:label_in})
        
        return df1
        
    def start(self,df2,lam,num):
        #Code starts here
        df_list = {}
        alpha = 1/num
        def add_one(x):
            return (x+lam*alpha)/(x.sum()+lam)
        
        #dfpivot2 = df2.pivot(index='cluster', columns='tp_id', values='tp_freq')

        label_in = df2[df2.columns[0]]
        df3 = df2[df2.columns[1:]]
        #label_in = df2.index.get_values()
        dfpivot4 = df3.fillna(0)
        dfpivot5 = dfpivot4.apply(add_one,axis=1)
        X = dfpivot5.as_matrix(columns=None)

        df = self.attr_clustering(X,label_in,'clusters')

        return df
