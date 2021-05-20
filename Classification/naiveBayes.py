# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 17:58:33 2020

@author: mahmoud saeed
"""
import numpy as np
import pandas as pd
##----------------------------------------------------
def separated_by_class(data , classes):
    data_dic = {}
    length = []
    unacc = data[data[6] == classes[0]]
    acc = data[data[6] == classes[1]]
    good = data[data[6] == classes[2]]
    vgood = data[data[6] == classes[3]]
    length.append(len(unacc))
    length.append(len(acc))
    length.append(len(good))
    length.append(len(vgood))
    for i in range(data.shape[1]-1):
        dic1 = {}
        unique_item = np.unique(np.array(data.iloc[:,i]))
        for j in unique_item:
            dic1[j] = []
            probability = len(unacc[unacc[i] == j])/len(unacc)
            dic1[j].append(probability)
            probability = len(acc[acc[i] == j])/len(acc)
            dic1[j].append(probability)
            probability = len(good[good[i] == j])/len(good)
            dic1[j].append(probability)
            probability = len(vgood[vgood[i] == j])/len(vgood)
            dic1[j].append(probability)
        data_dic[i] = dic1
    return data_dic , length
##---------------------------------------------------    
def predict(test_data , data , length):
    l = []
    for i in range(len(test_data)):
        dic = {}
        for k in range(len(length)):
            dic[k] = 1
        index = 0
        for j in test_data.iloc[i,0:6]:
            d = data[index][j]
            for k in range(len(d)):
                dic[k] *=d[k]
                
            index+=1
        index_of_max = max(dic, key=dic.get)
        l.append(index_of_max)
    return l 
##---------------------------------------------------

if __name__ == '__main__':
    
    print("hellow to our program")
    data = pd.read_csv("car.data.csv" ,header = None)
    unique = set(data.iloc[:,-1])
    data = data.sample(frac = 1)
    classes = list(unique)
    l = int(len(data)*0.75)
    train_data = data.head(l)
    test_data = data.tail(len(data)-l)
    new_data , length = separated_by_class(train_data , classes)
    #print(test_data)
    predict_index  = predict(test_data , new_data , length)
    print(len(predict_index),"   ",len(test_data))
    acu = 0
    for i in range(len(predict_index)):
        if test_data.iloc[i,-1] == classes[predict_index[i]]:
            acu +=1
        print("\nmy answer : ",classes[predict_index[i]])
        
        print("-------------------------")
    #print(new_data)   
    print("my accuracy is :"+str(round(acu/len(test_data)*100,2)))    
