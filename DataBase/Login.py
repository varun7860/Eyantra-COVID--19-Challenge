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

def update(data):
    new_user = input("Enter the username for your profile:  ")
    new_pass = input("Enter the password for your username:  ")
    new_user = str(new_user)
    new_pass = str(new_pass)
    connect = sqlite3.connect(data)
    curser = connect.cursor()
    curser.execute('''INSERT INTO  password (USERNAME,PASSWORD) values(?,?)''',(new_user,new_pass))
    connect.commit()
    new_database = pd.read_sql_query("SELECT * FROM password",connect)
    new_Items_list = list(new_database["USERNAME"])
    new_Quantity_list = list(new_database["PASSWORD"])
    new_dictionary = {new_Items_list[i]:new_Quantity_list[i] for i in range(len(new_Quantity_list))}
    return new_dictionary

def main():
    database = "  "  #Put the name of your database here
    dataframe = read_sql(database)
    Auth = read_excel(dataframe)
    
    for i in Auth:
      flag = -1
      login = input("enter your login id:  ")
      if login in Auth:
        print("username found")
        login = str(login)
        flag = 1
        break
      else:
        print("username not found")
        break
        
    if(flag == -1):
      confirm = input("Please Register to view Database(y/n):  ")  
      if(confirm == 'y'):
         Auth= update(database)
         print("Now please Refresh the Page and try logging in Again")
         flag = -2
      else:
         print("Database access denied") 
    
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
