
# Data Structure



+ ## Stock_analyze.py
  - ### 변수
    driver - selenium.webdriver.chrome.webdriver.WebDriver
    
    html - str
    
    soup - bs4.BeautifulSoup
    
    stock_set - dict
    
    sec - int
    
    tl_value - str
    
    tm_value - str
    
    rip_col - str
    
  - ### 함수
    
    parse_html : 크롤링한 문자열을 파싱
    
    create : 크롤링한 내용을 db에 저장
  
 
  - ### 라이브러리
   
    webdriver(selenium) : 웹크롤링을 위한 라이브러리
    
    pymysql : 파이썬 내에서 sql과 연동하기 위한 라이브러리
    
    BeautifulSoup : 웹크롤링한 내용을 문자열로 저장하기 위한 라이브러리
    
    re : 웹 크롤링한 내용 중 문자열로 전환 시 이모티콘 문자를 걸러내기 위해 사용되는 라이브러리



+ ## Stock_Db.sql
  - ### 테이블 구조
 



+ ## word_analyze.py
