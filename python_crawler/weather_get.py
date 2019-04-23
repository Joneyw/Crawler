import requests
import MySQLdb
from bs4 import BeautifulSoup

 # -------------------------------------爬取7天天气预报--------------------------------------#
 
def get_data(city_name):
    url = 'http://www.weather.com.cn/weather/'
    with open('city.txt','r') as fs:
        lines = fs.readlines()
        for line in lines:
            if(city_name in line):
                code = line.split('=')[0].strip()
                urls = url + code + '.shtml'
    try:    
        r = requests.get(urls, timeout=30)
        r.raise_for_status()      #异常判断 用法：https://www.jianshu.com/p/159bea26f7b5
        r.encoding = r.apparent_encoding
        html=r.text
    except:
        return '产生异常'

    weather_list = []
    soup = BeautifulSoup(html, 'html.parser')
    body = soup.body
    data = body.find('div', {'id': '7d'})
    ul = data.find('ul')
    lis = ul.find_all('li')
 
    for day in lis:
        temp_list = [city]
 
        date = day.find('h1').string
        temp_list.append(date)
 
        info = day.find_all('p')
        temp_list.append(info[0].string)
 
        if info[1].find('span') is None:
            temperature_highest = ' '
        else:
            temperature_highest = info[1].find('span').string
            temperature_highest = temperature_highest.replace('℃', ' ')
 
        if info[1].find('i') is None:  
            temperature_lowest = ' '
        else:
            temperature_lowest = info[1].find('i').string
            temperature_lowest = temperature_lowest.replace('℃', ' ')
 
        temp_list.append(temperature_highest)
        temp_list.append(temperature_lowest)
        weather_list.append(temp_list)
        
    return weather_list
 
# -------------------------------------写入数据库--------------------------------------#
def save_to_MySQL(result):
    print ("MySQL数据库存储中......")
    
    try:
        conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="mymovies", charset="utf8")
        cursor = conn.cursor()
        print ("数据库连接成功")        
        for i in range(100):
            sql=("insert into blog_weather(city,day,weather,temperature_high,temperature_lower) VALUES (%s,%s,%s,%s,%s)") 
            param=(result[i][0],result[i][1],result[i][2],result[i][3],result[i][4])
            cursor.execute(sql,param)
            conn.commit()      
        cursor.close()
        conn.close()
    except Exception as e:
        print (e)
    print ("MySQL数据库存储结束！")
# -------------------------------------清空数据库--------------------------------------#
def delete_to_MySQL():
        print("是否要清空历史数据库天气内容？是/否请按Y/N")
        get_input=input("")
        if get_input == "Y":           
                conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="mymovies", charset="utf8")
                cursor = conn.cursor()
                sql=("delete from blog_weather") 
                try:
                    cursor.execute(sql)
                    conn.commit()
                    print("delete OK")
                except:
                    conn.rollback()
                cursor.close()
                conn.close()        
               
        else :
            print("本次不清空历史数据！")
            
   
    
# -------------------------------------主模块--------------------------------------#
 
if __name__ == '__main__':
    delete_to_MySQL()
    cities="北京".split()  #选择要爬的城市
    print("-------------下面进行爬虫部分---------------")
    for city in cities:            
        data = get_data(city)    
        print(data)        
        save_to_MySQL(data)            
          
