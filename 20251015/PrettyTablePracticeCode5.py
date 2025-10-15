# -*- coding: utf-8 -*-
import sqlite3 as lite
from prettytable import from_db_cursor


if __name__ == '__main__':
    con = lite.connect('data.db')
    
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM product')
        table = from_db_cursor(cur) 
    
    print(table)