import sqlite3
from sqlite3 import Error
from oauth2client.service_account import ServiceAccountCredentials
import numpy as np
import pandas as pd

def excel():
    df = pd.read_excel(data_path, names =['No.','Item', 'Quantity'])
    Items_list = list(df["Item"])
    Quantity_list = list(df["Quantity"])
    dictionary = {Items_list[i]:Quantity_list[i] for i in range(len(Quantity_list))}
    identical_item = list(set(Items_list)&set(Quantity_list))
    return Items_list,Quantity_list, dictionary

def connection():
    con = None
    try:
        con = sqlite3.connect("Medicines_List.db")
        print("Connection Successful")
        return con
    except Error as e:
        print(e)

def Create_Table(con):
    curser = con.cursor()
    curser.execute("CREATE TABLE Supply(id integer PRIMARY KEY,MEDICINE text,QUANTITY integer)")
    curser.execute('''INSERT INTO  Supply VALUES(1,'TJM2',20)''')
    curser.execute('''INSERT INTO  Supply VALUES(2,'AT-100',300)''')
    curser.execute('''INSERT INTO  Supply VALUES(3,'TZLS-501',100)''')
    curser.execute('''INSERT INTO  Supply VALUES(4,'OYA1',56)''')
    curser.execute('''INSERT INTO  Supply VALUES(5,'BPI-002',75)''')
    curser.execute('''INSERT INTO  Supply VALUES(6,'INO-4800',10)''')
    curser.execute('''INSERT INTO  Supply VALUES(7,'NP-120',180)''')
    curser.execute('''INSERT INTO  Supply VALUES(8,'APN01',175)''')
    curser.execute('''INSERT INTO  Supply VALUES(9,'MRNA-1273',80)''')
    curser.execute('''INSERT INTO  Supply VALUES(10,'IBV',200)''')
    con.commit()

def main():
    con =  connection()
    Create_Table(con)
    

if __name__== "__main__":
    main()
    
