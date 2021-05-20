# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 15:39:01 2020

@author: mahmoud saeed
"""


import pandas as pd
import numpy as np
import csv
import itertools 
"""
colsnames = cofeeShop.columns
    length = len(cofeeShop)
    min_sup = min_sup * length
    UniqueItem = list(map(set,cofeeShop.values))
    df = pd.DataFrame(data = UniqueItem , columns = ['item1','item2','item3'])
    c1 = df['item1'].value_counts()
    c2 = df['item2'].value_counts()
    c3 = df['item3'].value_counts()                             
    

"""
def findsubsets(s, n): 
    return list(itertools.combinations(s, n))

def get_data(fileName , min_sup):
    cofeeShop = pd.read_excel(fileName)
    cofeeShop = cofeeShop[['Item1' , 'Item2','Item3']]
    length = len(cofeeShop)
    freq = []
    ##new_coffee = pd.DataFrame(columns = ['Item 1', 'Item 2', 'Item 3'])
    d = ['Brownie' , 'Cake' , 'CaramelBites', 'Chocolates',
             'Coffee', 'Cookies', 'Hot chocolate', 'Juice','Mineral water','Tea']
    for i in d:
        count = 0
        for j in range(len(cofeeShop)):
            if(i == cofeeShop.iloc[j,0] or i == cofeeShop.iloc[j,1]
               or i == cofeeShop.iloc[j,2]):
                count = count +1
        freq.append(count) 
    min_sup = length * min_sup    
    items = pd.DataFrame({'items':d , 'freq':freq})
    items = items[items['freq'] >= min_sup]
    items.to_excel(r'one_item.xlsx')
    ##print(items[['items']])
    print("save this data in file name 'one_item.xlsx'")
    return length

def getAllItemsFreq(min_sup , k):
     
    if(k > 3):
        return 0
    
    elif(k == 1):
        one_item = pd.read_excel("one_item.xlsx")
        coffeeShop = pd.read_excel("CoffeeShopTransactions.xlsx")
        coffeeShop = coffeeShop[['Item1','Item2','Item3']]
        length = len(coffeeShop)
        min_sup = length * min_sup
        item1 = []
        item2 = []
        freq = []
        data = findsubsets(one_item['items'], 2)
        for i in data:
            first_item = i[0]
            second_item = i[1]
            count = 0
            for k in range(len(coffeeShop)):
                if(first_item ==coffeeShop.iloc[k,0] or 
                      first_item ==coffeeShop.iloc[k,1] or
                      first_item ==coffeeShop.iloc[k,2]):
                       if(second_item ==coffeeShop.iloc[k,0] or 
                          second_item ==coffeeShop.iloc[k,1] or
                          second_item ==coffeeShop.iloc[k,2]):
                          count = count +1 
            item1.append(first_item)
            item2.append(second_item)
            freq.append(count)                
        items = pd.DataFrame({'item_1':item1,'item_2':item2,'freq':freq},
                             columns = ['item_1','item_2','freq'])        
        items = items[items['freq'] >= min_sup]
        items.to_excel(r'two_item.xlsx')
        print("save second file with name 'two_item.xlsx'")
        return len(items)
    else:
        one_item = pd.read_excel("one_item.xlsx")
        data = findsubsets(one_item['items'], 3)
        coffeeShop = pd.read_excel("CoffeeShopTransactions.xlsx")
        coffeeShop = coffeeShop[['Item1','Item2','Item3']]
        length = len(coffeeShop)
        min_sup = length * min_sup
        item1 = []
        item2 = []
        item3 = []
        freq = []
        for i in data:
            first_item = i[0]
            second_item = i[1]
            third = i[2]
            count = 0
            for k in range(len(coffeeShop)):
                if(first_item ==coffeeShop.iloc[k,0] or 
                   first_item ==coffeeShop.iloc[k,1] or
                   first_item ==coffeeShop.iloc[k,2]):
                    if(second_item ==coffeeShop.iloc[k,0] or 
                       second_item ==coffeeShop.iloc[k,1] or
                       second_item ==coffeeShop.iloc[k,2]):
                        if(third ==coffeeShop.iloc[k,0] or 
                           third ==coffeeShop.iloc[k,1] or
                           third ==coffeeShop.iloc[k,2]):
                            count = count +1 
            item1.append(first_item)
            item2.append(second_item)
            item3.append(third)
            freq.append(count)                
        items = pd.DataFrame({'item_1':item1,'item_2':item2,'item_3':item3,'freq':freq},
                             columns = ['item_1','item_2','item_3','freq'])        
        items = items[items['freq'] >= min_sup]
        items.to_excel(r'three_item.xlsx')
        print("save third file with name 'three_item.xlsx'")
        return len(items)
    
 
    
if __name__ == '__main__':
    print("hellow to our program")
    print("write minimum support  & minumum confidence in percent")
    ms = float(input())
    mc = float(input())
    length = get_data("CoffeeShopTransactions.xlsx"  , ms)
##    check = 1
    i = 1
   
    while(length > 0):
        length = getAllItemsFreq( ms , i)
        i = i+1
    print("last    ",i )
    if(i > 2):
        third = pd.read_excel('three_item.xlsx')
        second = pd.read_excel('two_item.xlsx')
        first = pd.read_excel('one_item.xlsx')
        if(i ==4):
            for i in range(len(third)):
                c1 = second.loc[(second['item_1']== third.iloc[i,0] or second['item_1']== third.iloc[i,1] )
                                 and(second['item_2']== third.iloc[i,0] or second['item_2']== third.iloc[i,1])
                                 ]['freq'].values
##                c2 = first.iloc[first['items']==third.iloc[i,2],2]     
                c3 = first.loc[first['items']==third.iloc[i,0]]['freq'].values
##                c4 = second.iloc[(second['item_1']== third.iloc[i,1] or second['item_1']== third.iloc[i,2] )
##                                 and(second['item_2']== third.iloc[i,1] or second['item_2']== third.iloc[i,2])
##                                 ,3]
                if(third.iloc[i,3]/c1 >= mc):
                    print("{",third.iloc[i,0]," , " ,third.iloc[i,1],"}  =>  ",third.iloc[i,2])
                if(third.iloc[i,3]/c3 >= mc):
                    print(third.iloc[i,0],"  =>  {" ,third.iloc[i,1]," , ",third.iloc[i,2],"}")
        
        for i in range(len(second)):
            c1 = first.loc[first['items'] == second.iloc[i,1]]['freq'].values
            c2 = first.loc[first['items'] == second.iloc[i,2]]['freq'].values
            c3 = second.iloc[i,3]
            if(c3/c1 >= mc):
                print(second.iloc[i,1],"   =>   ",second.iloc[i,2])
                print(c3/c1)
            
            if(c3/c2 >= mc):
                
                print(second.iloc[i,2],"   =>   ",second.iloc[i,1])  
                print(c3/c2)
    else:
        print('there is no item bigger than or equal minimum support and confidence')
    
        
 
     
##value.count
    
"""dic = {}
for item in df:
    dic[i] = c1.loc
"""

    