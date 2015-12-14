import pandas as pd
import numpy as np
import xlrd
from sqlalchemy import create_engine
k = pd.read_excel('terrorismtest.xlsx')

engine = create_engine('postgresql://username:password@localhost:5432/terrorism')


locationdata= k[['eventid','iyear','imonth','iday','country','city','latitude','longitude']]
attackdata = k[['eventid','gname','attacktype1','suicide','nperps','weaptype1','weapdetail']]
print(locationdata)
locationdata.to_sql('locations', engine, if_exists = 'append', chunksize = 1000)
attackdata.to_sql('attacks',engine,if_exists='append',chunksize = 1000)
