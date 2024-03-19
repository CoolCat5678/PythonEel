import eel
import sqlite3

con = sqlite3.connect("toten.db")
cur = con.cursor()

@eel.expose
def SqlExec(word):
    res = cur.execute(word)
    return f'{res.fetchone()}'


eel.init('web')
eel.start('main.html',size = (400,600))