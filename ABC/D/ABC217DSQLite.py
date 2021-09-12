import bisect
import sqlite3
#参考記事:https://qiita.com/saira/items/e08c8849cea6c3b5eb0c
#参考記事:https://nagiss.hateblo.jp/entry/2020/06/28/012528
#参考ツイート:https://twitter.com/zat22859390/status/1434329502935519236?s=20
#参考記事:https://www.dbonline.jp/sqlite/index/index2.html
conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute('CREATE TABLE cuts(length INTEGER)')
cur.execute('create INDEX lengthindex on cuts(length);')
L,Q = map(int,input().split())
cur.execute('INSERT INTO cuts VALUES (?)',(0,))
cur.execute('INSERT INTO cuts VALUES (?)',(L,))
for _ in range(Q):
    c,x = map(int,input().split())
    if c == 1:
        cur.execute('INSERT INTO cuts VALUES (?)',(x,))
    else:
        cur.execute("SELECT MAX(length) FROM cuts WHERE length < ?", (x, ))
        a = cur.fetchall()[0][0]
        cur.execute("SELECT MIN(length) FROM cuts WHERE length > ?", (x, ))
        b = cur.fetchall()[0][0]
        print(b-a)