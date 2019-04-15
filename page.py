from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import time
import MySQLdb

driver=webdriver.Chrome(r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe')
wait=WebDriverWait(driver,100)
driver.get('https://www.jd.com/')

def search():
    print("搜索中")
    try:
        input=wait.until(
            EC.presence_of_element_located((By.ID,'key'))
        )
        input.send_keys('{}'.format("手机"))
        submit=wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,'#search > div > div.form > button'))
        )
        submit.click()   
        get_JD()          
    except TimeoutException:
        return search()    

def get_JD():    
   
    
    try:
        skus = wait.until(EC.presence_of_all_elements_located((By.XPATH,'//li[@class="gl-item"]')))
        skus = [item.get_attribute('data-sku') for item in skus]
        names=wait.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="gl-i-wrap"]/div[4]/a/em')))
        prices=wait.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="gl-i-wrap"]/div[3]/strong/i')))
        comments=wait.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="gl-i-wrap"]/div[5]/strong')))                 

        jd_list=[]         
        links=['https://item.jd.com/{sku}.html'.format(sku=item) for item in skus]
        names=[i.text for i in names]
        prices=[i.text for i in prices]
        comments=[i.text for i in comments]      
        ha=zip(names,prices,comments,links)
 
        for h in ha:
            jd_list.append(list(h))
            print(h)
       # print(jd_list)
            
        return jd_list    
    except TimeoutException:
        return get_JD()   

def turn_page():   
    try:
        #实现下一页跳转点击
        wait.until(EC.element_to_be_clickable((By.XPATH,'//a[@class="pn-next"]'))).click() 
        time.sleep(2)
        #实现滚动条下拉，跳转至第二页
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        
        

    except TimeoutException:
        return turn_page()    
# -------------------------------------写入数据库--------------------------------------#
def save_to_MySQL(result):
    print ("MySQL数据库存储中......")
    
    try:
        conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="mymovies", charset="utf8")
        cursor = conn.cursor()
        print ("数据库连接成功")
      #  for h in result:
      #      print('link：' + str(h[0]) + '\n')
      #      print('name：' + str(h[1]) + '\n')
      #      print('price：' + str(h[2]) + '\n')
      #      print('comment：' + str(h[3]) + '\n')           
      #      print('-------------------------------------------------------------------')        
        for i in range(100):
            sql=("insert into blog_jd_goods(name,price,comment,link) VALUES (%s,%s,%s,%s)") 
            param=(result[i][0],result[i][1],result[i][2],result[i][3])
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
                sql=("delete from blog_jd_goods") 
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
if __name__=='__main__':
    num=0
    delete_to_MySQL()
    search()
    
    for i in range(250):
        num +=1
        print("正在爬取第{}页".format(num))
        r=get_JD()
        save_to_MySQL(r)
        turn_page()
        time.sleep(10)
        