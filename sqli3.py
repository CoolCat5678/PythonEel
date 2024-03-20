import eel
import sqlite3

con = sqlite3.connect("toten.db")
cur = con.cursor()

# 控制是否需要commit rollback
con.isolation_level = None

@eel.expose
def load():
    ID = cur.execute('SELECT ID FROM Customer')
    return ID.fetchall()
# PRAGMA table_info(table_name);

@eel.expose
def SqlExec(word):
    r = ''
    res = cur.execute(word)
    for i in res.fetchall():
        r += str(i)
        
    return f'{r}'

@eel.expose
def SelectID(ID):
    r = ''
    strSQL = f"SELECT C.ID, T.TradeDate, T.Amount FROM Customer C LEFT JOIN TradeHis T ON C.ID=T.ID WHERE C.ID='{ID}'"
    res = cur.execute(strSQL)
    for i in res.fetchall():
        r += str(i) + '\r' 
        
    return f'{r}'

eel.init('web')
eel.start('main.html',size = (1000,600))