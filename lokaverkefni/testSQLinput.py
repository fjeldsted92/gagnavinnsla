import pandas as pd
import numpy as np
import xlrd
from sqlalchemy import create_engine
k = pd.read_excel('terrorismtest.xlsx')

engine = create_engine('postgresql://USERNAME:PASSWORD@localhost:5432/terrorism')


locationdata= k[['eventid','iyear','imonth','iday','country','city','latitude','longitude']]
attackdata = k[['eventid','gname','attacktype1','suicide','nperps','weaptype1','weapdetail']]
targetdata = k[['eventid', 'targtype1', 'targsubtype1', 'target1', 'natlty1','nkill']]
commentdata = k[['eventid','summary','motive','addnotes']]
countrykeydata = k[['country','country_txt']].drop_duplicates()
attackkeydata = k[['attacktype1', 'attacktype1_txt']].drop_duplicates()
targetkeydata = k[['targtype1','targtype1_txt']].drop_duplicates()
targsubkeydata = k[['targsubtype1','targsubtype1_txt']].drop_duplicates()
weaponkeydata = k[['weaptype1','weaptype1_txt']].drop_duplicates()

locationdata.to_sql('locations', engine, if_exists = 'replace', chunksize = 1000)
attackdata.to_sql('attacks',engine,if_exists='replace',chunksize = 1000)
targetdata.to_sql('targets',engine,if_exists='replace',chunksize = 1000)
commentdata.to_sql('comments',engine,if_exists='replace',chunksize = 1000)
countrykeydata.to_sql('countrykey',engine,if_exists='replace',chunksize = 1000)
attackkeydata.to_sql('attackkey',engine,if_exists='replace',chunksize = 1000)
targetkeydata.to_sql('targetkey',engine,if_exists='replace',chunksize = 1000)
targsubkeydata.to_sql('targsubkey',engine,if_exists='replace',chunksize = 1000)
weaponkeydata.to_sql('weaponkey',engine,if_exists='replace',chunksize = 1000)
