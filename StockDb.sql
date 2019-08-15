create table board_collecting(
   WriteDate varchar(70) not null primary key,
   Title varchar(70) ,
   contents varchar(3000),
   ripple varchar(4000)) engine=InnoDb default character set= utf8;
   delete from board_collecting;
    SET SQL_SAFE_UPDATES = 0;
select * from board_collecting 
