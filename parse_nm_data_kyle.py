import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.pylab as pylab

active_nm=pd.read_csv('active_wells_NM.csv', sep=',')

nm_database=pd.read_csv('AllWells-NM.csv')
nm_database.rename(index=str, columns={"API": "API_NO"}, inplace=True)

##Drop last three digits from active well file
active_nm.API_NO=active_nm.API_NO.str.slice(start=0, stop=12)
##remove dashes
active_nm.API_NO=active_nm.API_NO.str.replace('-','')
print 'total active wells'
print active_nm.API_NO.count()

#convert column type to match database
active_nm.API_NO=active_nm['API_NO'].astype(str).astype(int)

nm_database.drop(labels=['ACRES', 'OPERATOR',
       'PRODUCING_POOLID', 'PROPERTY', 'RANGE', 'SDIV_UL',
       'SECTION',  'TOWNSHIP', 'TVD_DEPTH', 'water_inj_2016',
       'water_inj_2017', 'water_inj_2018', 'water_prod_2016',
       'water_prod_2017', 'water_prod_2018', 'WELL_NAME', 'WELL_TYPE',
       'COMPL_STATUS', 'COUNTY', 'days_prod_2016', 'days_prod_2017',
       'days_prod_2018', 'ELEVGL', 'EW_CD', 'FTG_EW', 'FTG_NS',
       'gas_prod_2016', 'gas_prod_2017', 'gas_prod_2018',
       'LAST_PROD_INJ', 'LATITUDE', 'LONGITUDE', 'NBR_COMPLS', 'NS_CD',
       'OCD_UL', 'OGRID_CDE', 'oil_prod_2016', 'oil_prod_2017',
       'oil_prod_2018', 'ONE_PRODUCING_POOL_NAME'], axis=1, inplace=True)

#r=active_nm.merge(nm_database, how='left', on='API_NO')
r=nm_database.merge(active_nm, how='left', on='API_NO')



