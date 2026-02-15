import sqlite3
conn=sqlite3.connect('sugizaki.db')
cur=conn.cursor()

cur.execute('''CREATE TABLE tyumon (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hinban_id INTEGER,
    kosuu INTEGER,
    meibo_id INTEGER,
    nitizi text default (datetime('now','localtime')),
    tyumonzikakaku integer,
    jotai text,
    foreign key (hinban_id) references hinban(id),
    foreign key (meibo_id) references meibo(id)
);''') 
cur.execute('''
            INSERT INTO tyumon(hinban_id,kosuu,meibo_id,tyumonzikakaku,jotai) VALUES(3,1,10,180,"未入荷")'''
            )
cur.execute('''
            INSERT INTO tyumon(hinban_id,kosuu,meibo_id,tyumonzikakaku,jotai) VALUES(1,2,15,88000,"未入荷")'''
            )
conn.commit()
conn.close()