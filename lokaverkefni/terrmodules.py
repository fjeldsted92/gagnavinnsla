#N: Gets data form the database for dates between date 1 and date 2
#F: date1, date2 = "yyyy:mm:yy"
#E: returns selected data from database between dates date1 and date2
def point_Data_Get(date1, date2,cursoritem):
    cursoritem.execute("SELECT  l.latitude, l.longitude, l.eventid, l.iyear, l.imonth, l.iday, ck.country_txt, l.city, ak.attacktype1_txt, a.suicide, a.gname, a.nperps,tk.targtype1_txt,t.nkill FROM locations l, attacks a, targets t, attackkey ak, targetkey tk, countrykey ck WHERE l.eventid = a.eventid AND l.eventid = t.eventid and t.targtype1 = tk.targtype1 and ck.country = l.country and ak.attacktype1 = a.attacktype1 and a.eventid BETWEEN (%s) AND (%s);",(self.date_a,self.date_b))
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

# int a
def top_X_deadly(a):
    cursoritem.execute("select t.nkill as casulalities, l.city, l.iday, l.imonth, l.iyear, a.gname as groupname, att.attacktype1_txt as AttackType, w.weaptype1_txt as Weapons, c.summary, c.motive from targets t, locations l, attacks a, attackkey att, weaponkey w, comments c where t.eventid = l.eventid and t.eventid = a.eventid and att.attacktype1 = a.attacktype1 and w.weaptype1 = a.weaptype1 and c.eventid = a.eventid and t.nkill is not null order by t.nkill desc limit (%s);",(int(a)))
    c = cursoritem.fetchall()
    return c

#N: f = pointdatacsv.csv
#F: date1, date2 = "YYYY:MM:DD"
#E: pointdatacsv.csv contains the selected data in csv format
def point_file_write(date1, date2, cursoritem):
    f = open('pointdatacsv.csv','w', encoding = 'utf8')
    date_a, date_b = date_format_correcter(date1, date2)
    k = point_Data_Get(date_a, date_b,cursoritem)
    f.write('latitude,longitude,eventid,iyear,imonth,iday,country_txt,city,attacktype1_txt,suicide,gname,nperps,targtype1_txt,nkill\n')
    for i in k:
        l = []
        for j in range(13):
            f.write(str(i[j])+',')
        f.write(str(i[13]))
        f.write('\n')
