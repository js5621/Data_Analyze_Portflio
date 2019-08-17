import pymysql
from konlpy.tag import Twitter
from collections import Counter
import pytagcloud
conn = pymysql.connect(host='localhost', user='asph5621', password='js930',
                     db='StckDb', charset='utf8') # pymysql 라이브러리의 connect 함수를 이용해 mysql의 StckDb와 연결
str1=""
str2=""
strx=""
try:
    with conn.cursor() as cursor:#
        sql = 'select Title,contents,ripple from board_collecting where WriteDate like \'%2019-08%\' order by WriteDate asc' 
        cursor.execute(sql)
        conn.commit()#  board_collecting 테이블에 크롤링한 게시글,작성 날자,제목,내용,댓글을 삽입(작성 날짜가 primary key)           
        rows=cursor.fetchall()
        
        
        for i in range(0,len(rows)):
            strx+=rows[i][0]+" "+rows[i][1]+" "+rows[i][2]
        
finally:
    conn.close()
        

twitter = Twitter()
nouns= twitter.nouns(strx)

count =Counter(nouns)
del_dic=['이','요','등','좀','전','떼','저','그','분','중','주','제','거','글','때문','종목','것','생각','주식','투자']

for word in del_dic:
    del count[word]


count
tag_A=count.most_common(50)
taglist = pytagcloud.make_tags(tag_A, maxsize=80)
pytagcloud.create_tag_image(taglist, 'C:/Users/family/Desktop/WordCloudimage/AugustWord.jpg', size=(900, 600), fontname='Korean', rectangular=False)
