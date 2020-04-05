import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#this code plots and calculates statistics for the ratio between the initial production volume and post-refrac production volume for basins.  Plots and statistics are split by wells where the initial production volume was higher than the post refrac volume and those where the post refrac volume was higher.  

basins=['anadarko']#, 'arkoma', 'delaware', 'dj', 'east_texas', 'fort_worth', 'gulf_coast', 'marcellus', 'mid_continent', 'midland', 'piance', 'san_juan', 'williston']

for basin in basins:
    print basin
    all_data=pd.read_csv(basin+'_all_c.csv')
    all_data_refrac=all_data[all_data.refracFlag == 'YES'] #picks wells that have been refracked
    all_data_refrac_uniqueAPI=all_data_refrac.groupby(by='api10').max()  #many wells have multiple (nearly identical) entries so grouping them into unique api's so we don't count the same well multiple times
    a=all_data_refrac_uniqueAPI[all_data_refrac_uniqueAPI['oilIPRatio'] < 1].groupby(by='wellbore').oilIPRatio.describe() # calculates statistics for oil ratios where post refrac volume is lower than initial
    all_data_refrac_uniqueAPI[all_data_refrac_uniqueAPI['oilIPRatio'] < 1].boxplot(column='oilIPRatio', by='wellbore') #plots data
    plt.savefig('oilIPRlt1_'+basin+'.png')
    plt.close()
    a['id']='oilipratio < 1'   # a is the dataframe that will hold all the output from describe() 
    a['basin']=basin
    
    b=all_data_refrac_uniqueAPI[all_data_refrac_uniqueAPI['oilIPRatio'] > 1].groupby(by='wellbore').oilIPRatio.describe()  #same as above, but for wells where oil refrac volume is larger than initial volume
    all_data_refrac_uniqueAPI[all_data_refrac_uniqueAPI['oilIPRatio'] > 1].boxplot(column='oilIPRatio', by='wellbore')
    plt.savefig('oilIPRgt1_'+basin+'.png')   
    plt.close()  
    b['id']='oilipratio > 1'
    b['basin']=basin
    a=a.append(b) #adding this data to dataframe a
    
    b=all_data_refrac_uniqueAPI[all_data_refrac_uniqueAPI['gasIPRatio'] < 1].groupby(by='wellbore').gasIPRatio.describe()#same as above, but for wells where gas refrac volume is smaller than initial volume
    all_data_refrac_uniqueAPI[all_data_refrac_uniqueAPI['gasIPRatio'] < 1].boxplot(column='gasIPRatio', by='wellbore')
    plt.savefig('gasIPRlt1_'+basin+'.png')   
    plt.close() 
    b['id']='gasipratio < 1'
    b['basin']=basin 
    a=a.append(b) 
    
    b=all_data_refrac_uniqueAPI[all_data_refrac_uniqueAPI['gasIPRatio'] > 1].groupby(by='wellbore').gasIPRatio.describe()#same as above, but for wells where gas refrac volume is larger than initial volume
    all_data_refrac_uniqueAPI[all_data_refrac_uniqueAPI['gasIPRatio'] > 1].boxplot(column='gasIPRatio', by='wellbore')
    plt.savefig('gasIPRgt1_'+basin+'.png')   
    plt.close()
    b['id']='gasipratio > 1'
    b['basin']=basin
    a=a.append(b)
    
    a.to_csv(basin+'_refrac_stats.csv')
    

    print basin
    