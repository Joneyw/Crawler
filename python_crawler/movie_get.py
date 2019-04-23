#coding=utf-8
import MySQLdb
from lxml import etree
import requests
import time

nameList=[]
scoreList=[]
hrefList=[]
numberList=[]
scribleList=[]

def get_movie():
    for a in range(10):
        url = 'https://movie.douban.com/top250?start={}'.format(a*25)
        data = requests.get(url).text
        # print(data)
        s = etree.HTML(data)
        file = s.xpath('//*[@id="content"]/div/div[1]/ol/li')
        for div in file:   
             movies_name = div.xpath('./div/div[2]/div[1]/a/span[1]/text()')[0]
             movies_score = div.xpath('./div/div[2]/div[2]/div/span[2]/text()')[0]             
             movies_number = div.xpath('./div/div[2]/div[2]/div/span[4]/text()')[0].strip("(").strip( ).strip(")")
             movie_scrible = div.xpath('./div/div[2]/div[2]/p[2]/span/text()')
             # time.sleep(1)
             nameList.append(movies_name)
             scoreList.append(movies_score)           
             numberList.append(movies_number)
             if(movie_scrible):
                scribleList.append(movie_scrible)
             else:
                scribleList.append("无")
            
       
            
    print("恭喜，爬虫已完毕！")   
    return nameList,scoreList,numberList,scribleList
def save_to_MySQL():
    print ("MySQL数据库存储中......")
    
    try:
        conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="mymovies", charset="utf8")
        cursor = conn.cursor()
        print ("数据库连接成功")
        for i in range(260):
            sql=("insert into blog_movie VALUES (%s,%s,%s,%s,%s)") 
            param=(i+1,nameList[i],scoreList[i],numberList[i],scribleList[i])
            cursor.execute(sql,param)
            conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print (e)
    print ("MySQL数据库存储结束！")

    # -------------------------------------主模块--------------------------------------#
if __name__=="__main__":
    get_movie()
    save_to_MySQL()