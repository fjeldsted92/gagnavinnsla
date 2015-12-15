import pandas as pd
import numpy as np
import xlrd
from sqlalchemy import create_engine
import psycopg2
host = 'localhost'
dbname = 'terrorism'
username = 'postgres'
#pw = getpass.getpass()
pw = 'answer43'
conn_string = "host='{}' dbname='{}' user='{}' password='{}'".format(host, dbname, username, pw)
print("Connecting to database {}.{} as {}".format(host, dbname, username))
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()
print("Connected!\n")

k = pd.read_excel('globalterrorismdb_0615dist.xlsx')
engine = create_engine('postgresql://postgres:answer43@localhost:5432/terrorism')
k = k.dropna(subset = ['latitude', 'longitude'], how = 'any')  #droppum -llum atburðum sem ekki hafa hnit
locationdata= k[['eventid','iyear','imonth','iday','country','city','latitude','longitude']]
attackdata = k[['eventid','gname','attacktype1','suicide','nperps','weaptype1','weapdetail']]
targetdata = k[['eventid', 'targtype1', 'targsubtype1', 'target1', 'natlty1','nkill']]                      #keep natltly1?
commentdata = k[['eventid','summary','motive','addnotes']].dropna(subset = ['summary'], how = 'all')
countrykeydata = k[['country','country_txt']].drop_duplicates().dropna()
attackkeydata = k[['attacktype1', 'attacktype1_txt']].drop_duplicates().dropna()
targetkeydata = k[['targtype1','targtype1_txt']].drop_duplicates().dropna()
targsubkeydata = k[['targsubtype1','targsubtype1_txt']].drop_duplicates().dropna()
weaponkeydata = k[['weaptype1','weaptype1_txt']].drop_duplicates().dropna()
locationdata.to_sql('locations', engine, if_exists = 'replace', chunksize = 1000)
attackdata.to_sql('attacks',engine,if_exists='replace',chunksize = 1000)
targetdata.to_sql('targets',engine,if_exists='replace',chunksize = 1000)
commentdata.to_sql('comments',engine,if_exists='replace',chunksize = 1000)
countrykeydata.to_sql('countrykey',engine,if_exists='replace',chunksize = 1000)
attackkeydata.to_sql('attackkey',engine,if_exists='replace',chunksize = 1000)
targetkeydata.to_sql('targetkey',engine,if_exists='replace',chunksize = 1000)
targsubkeydata.to_sql('targsubkey',engine,if_exists='replace',chunksize = 1000)
weaponkeydata.to_sql('weaponkey',engine,if_exists='replace',chunksize = 1000)

f = open('indexes.txt','r')
for row in f:
    cursor.execute(row)
    print(row)
conn.commit()
