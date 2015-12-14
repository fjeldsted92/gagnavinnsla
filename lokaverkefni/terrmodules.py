import psycopg2

def Connect():

    host = 'localhost'
    dbname = 'terrorism'

    username = 'postgres'
    #pw = getpass.getpass()
    pw = 'answer43'
    conn_string = "host='{}' dbname='{}' user='{}' password='{}'".format(host, dbname, username, pw)

    print("Connecting to database {}.{} as {}".format(host, dbname, username))

    conn = psycopg2.connect(conn_string)
    curs = conn.cursor()
    return curs
#N: Gets data form the database for dates between date 1 and date 2
#F: date1, date2 = "yyyy:mm:yy"
#E: returns selected data from database between dates date1 and date2
def point_Data_Get(date1, date2,cursoritem):
    cursoritem.execute("SELECT locations.eventid, locations.iyear, locations.imonth, locations.iday,  locations.city, locations.latitude, locations.longitude  FROM locations WHERE (locations.eventid BETWEEN (%s) AND (%s));", (date1, date2))
    c = cursoritem.fetchall()
    return c

#N: date A, date B = date_format_correcter(date1,date2)
#F: date1, date 2 er á formi 'YYYY:MM:DD'
#E: date A , B eru á formi ´YYYYMMDD0000´ svo það virkar sem samanburður við eventid
def date_format_correcter(date1, date2):
    print(date1)
    date1hold = date1.split(sep = ':')
    print(date1hold)
    date1hold.append('0000')
    print(date1hold)
    date2hold = date2.split(sep = ':')
    date2hold.append('0000')
    date1hold = ''.join(date1hold)
    date2hold = ''.join(date2hold)
    return date1hold, date2hold



#N: f = pointdatacsv.csv
#F: date1, date2 = "dd:mm:yyyy"
#E: pointdatacsv.csv contains the selected data in csv format
def point_file_write(date1, date2, cursoritem):
    f= open('pointdatacsv.csv','w')
    date_a, date_b = date_format_correcter(date1, date2)
    k = point_Data_Get(date_a, date_b,cursoritem)
    for i in k:
        print(i)
    f.close()
a = '2011:11:12'
b = '2011:12:12'
print(date_format_correcter(a,b))
curs = Connect()
point_file_write(a,b,curs)