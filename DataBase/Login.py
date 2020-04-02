import sqlite3
import pandas as pd
import numpy as np

def read_excel(df):
    Items_list = list(df["USERNAME"])
    Quantity_list = list(df["PASSWORD"])
    dictionary = {Items_list[i]:Quantity_list[i] for i in range(len(Quantity_list))}
    return dictionary

def read_sql(data):
    con = sqlite3.connect(data)
    df = pd.read_sql_query("SELECT * FROM password",con)
    return df

def main():
    database = "  "  #Put the name of your database here
    dataframe = read_sql(database)
    Auth = read_excel(dataframe)
    
    for i in Auth:
      login = input("enter your login id:  ")
      if login in Auth:
        print("username found")
        login = str(login)
        flag = 1
        break
      else:
        print("username not found")
    print("Too Many Tries Logging in")    
    while(flag ==1):
       x = Auth.get(login)
       password = input("enter your password:  ")
       password = str(password)
       if(password == x):
         print("Password Confirmed")
         flag = 2
         break
       else:
         print("Wrong Password")
    
    if(flag==2):
        print("login successful")
           
           
if __name__ == "__main__":
    main()
