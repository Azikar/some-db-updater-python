import pymysql
import requests
from bs4 import BeautifulSoup
import time

class object:
    def __init__(self, id,name,lastname,ident):
        self.id=id
        self.name=name
        self.lastname=lastname
        self.ident=ident

def main():
    #object=object()
    while True:
        try:
            r=requests.get('http://localhost:8080/Training2/ReadFrom.php')
            
            conn=pymysql.connect(host="localhost",user="root",passwd="",database="training2")
            
            soup=BeautifulSoup(r.text,'html.parser')
            result=soup.find_all('li')
            a=[]
            print(len(result)/4)
            for x in result:
                new=x.find_all('li')
                if len(new)>0:
                    obj=object(new[0].contents,new[1].contents,new[2].contents,new[3].contents);
                    a.append(obj)
                    #print(new[0].contents)
            b=conn.cursor()
            b.execute("DELETE FROM `data`")
            conn.commit()
            
            
            for x in a:
                #cursor=conn.cursor()
                sql = "INSERT INTO `data` (`id`, `name`, `Last_name`, `Unique identifier`) VALUES (%s, %s, %s, %s)"
                b.execute(sql, (x.id,x.name,x.lastname,x.ident))
                conn.commit()
            b.close()
            print("im oky")
            time.sleep(10)
        except:
            print("ops")
            time.sleep(10)
#print(result[6:10])
#print(result);
#a=conn.cursor()
if __name__ == "__main__":
    main()
