# -*- coding: UTF-8 -*-
import csv
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
import pymysql
import re



def parse_html(slc,soup): # Beatiful soup으로  html selector의 주소에 있는 문자열 값을 파싱하여 ht_value 값으로 반환하는 합수
                          # slc 는 html selector 값 soup는 beatifulSoup의 htmlparser 기능을 사용한 함수
    tls=soup.select(slc) 
    ht_value=''
    for ti in tls: # start
        if not ti.string is None:
            ht_value= ht_value+'\n'+ti.string    
        time.sleep(sec)# end  html을 파싱하여  문자열 변수  ht_value에 저장 
    return ht_value  # 저장 한 ht_value를 반환 

def create(time,title,contents,ripple): # time:크롤링한 게시글의 작성시간 , title:게시글 제목 contents: 해당 게시글의 내용 ripple: 해당 게시글의 댓글 모음
       
          
    conn = pymysql.connect(host='localhost', user='asph5621', password='js930',
                       db='StckDb', charset='utf8') # pymysql 라이브러리의 connect 함수를 이용해 mysql의 StckDb와 연결
    try:
        with conn.cursor() as cursor:#
            sql = 'INSERT INTO board_collecting (WriteDate, Title, contents,ripple) VALUES (%s, %s,%s,%s)' 
            cursor.execute(sql,(time,title,contents, ripple))
            conn.commit()#  board_collecting 테이블에 크롤링한 게시글,작성 날자,제목,내용,댓글을 삽입(작성 날짜가 primary key)           
            
       
    finally:
        conn.close()
        
         



driver=webdriver.Chrome('D:\chromdriver\chromedriver.exe') #크롬 드라이버 호출 

for pge in range(0,25):
  
    driver.get('https://www.clien.net/service/board/cm_stock?&od=T31&po='+str(pge)) # 변수 값에 해당하는 페이지로 이동
    html = driver.page_source #드라이버로 이동 된 웹 페이지의 html을 html 변수에 저장 
    soup = BeautifulSoup(html, 'html.parser') # BeautifulSoup 의 html parser에 html을 넣고 반환 된 값을 soup변수에 저장

    sec = 1
    stock_set={}

    for  tis in range(14,44):
        html = driver.page_source #드라이버로 이동 된 웹 페이지의 html을 html 변수에 저장 

        soup = BeautifulSoup(html, 'html.parser') # BeautifulSoup 의 html parser에 html을 넣고 반환 된 값을 soup변수에 저장



        time.sleep(sec) # 1초간 멈춤
       
        tl_value=parse_html( "#div_content > div:nth-child("+str(tis)+") > div.list_title > a > span.subject_fixed",soup) # 게시글 제목이 있는
                                                                                                                          #html selector값과 soup변수를 parse_html변수에 집어넣고
                                                                                                                          # 반환되는 문자열 값을 tl_value에 저장  
    
        print(tl_value)
        time.sleep(sec)
   
  
    
    

        tm_value= parse_html("#div_content > div:nth-child("+str(tis)+") > div.list_time > span > span",soup) # 게시글 작성 시간이 있는
                                                                                                              #html selector값과 soup변수를 parse_html변수에 집어넣고
                                                                                                              # 반환되는 문자열 값을 tm_value에 저장  

        print(tm_value)

        time.sleep(sec)
   
    
    
        driver.find_element_by_xpath('//*[@id="div_content"]/div['+str(tis)+']/div[2]/a[1]/span[2]').click() #게시글 제목 클릭

        time.sleep(sec)

        html = driver.page_source

        soup = BeautifulSoup(html, 'html.parser')

        tot_sen=parse_html("#div_content > div.post_view > div.post_content > article > div > p",soup) # 게시글 내용이 있는
                                                                                                       #html selector값과 soup변수를 parse_html변수에 집어넣고
                                                                                                       # 반환되는 문자열 값을 tot_sen에 저장  

        print(tot_sen)

            
        
   
        time.sleep(sec)

        rip_col=''
        rip_count=parse_html("#comment-point > span:nth-child(1) > strong",soup) # 게시글 댓글 수가있는
                                                                                 #html selector값과 soup변수를 parse_html변수에 집어넣고 반환되는 문자열 값을 rip_count 에 저장 

        if int(rip_count) == 0: # 게시글 댓글수를 정수로 바꿔서 댓글수 가 0인경우 rip_col변수에  "댓글 없음" 값을 삽입
            rip_col = '댓글 없음'
    
        else: # 댓글수가 0일 아닐경우
            rip_col=parse_html("#div_content > div.post_comment > div.comment > div> div.comment_content > div > p",soup) # 게시글   댓글이 있는
                                                                                                                          #html selector값과 soup변수를 parse_html변수에 집어넣고
                                                                                                                          # 반환되는 문자열 값을 rip_col에 저장  
            EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
            rip_col = EMOJI.sub(r'', rip_col)
        print(rip_col)

        create(tm_value,tl_value,tot_sen,rip_col) # create 함수를 호출하여  크롤링 한 내용을 sql에 저장

        time.sleep(sec)
    

        driver.find_element_by_xpath('//*[@id="div_content"]/div[6]/a/span[2]').click() # 다시 게시글 리스트로 가는 버튼 클릭

        time.sleep(sec)

    




