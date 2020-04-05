import numpy
import numpy as np
import sqlite3
import pandas as pd


def read_excel(df):
    Items_list = list(df["USERNAME"])
    Quantity_list = list(df["PASSWORD"])
    dictionary = {Items_list[i]:Quantity_list[i] for i in range(len(Quantity_list))}
    return Items_list,Quantity_list,dictionary

def read_sql(data):
    con = sqlite3.connect(data)
    df = pd.read_sql_query("SELECT * FROM Personal",con)
    return df

def update(data):
    new_user = input("Enter the username for your profile:  ")
    new_pass = input("Enter the password for your username:  ")
    new_user = str(new_user)
    new_pass = str(new_pass)
    connect = sqlite3.connect(data)
    curser = connect.cursor()
    curser.execute('''INSERT INTO  Personal (USERNAME,PASSWORD) values(?,?)''',(new_user,new_pass))
    connect.commit()
    new_database = pd.read_sql_query("SELECT * FROM Personal",connect)
    new_Items_list = list(new_database["USERNAME"])
    new_Quantity_list = list(new_database["PASSWORD"])
    new_dictionary = {new_Items_list[i]:new_Quantity_list[i] for i in range(len(new_Quantity_list))}
    return new_dictionary

def new_login(Dict):
     for i in Dict:
       flag = -1
       login = input("enter your login id:  ")
       if login in Dict:
         print("username found")
         login = str(login)
         flag = 1
         break
       else:
         print("username not found")
         break

     return login

def supplies(data,Dict):
    ID = input("enter your current username:  ")
    if ID in Dict:
        sanitiser = input("Enter the Quantity of sanitiser you have: " )
        beds = input("Enter the Quantity of beds you have:  ")
        Masks = input("Enter the Quantity of Masks you have:  ")
        vitamin_C = input("Enter the Quantity of vitaminC supplies you have:  ")
        vitamin_B12 = input("Enter the Quantity of vitaminB12 supplies you have:  ")
        ppe = input("Enter the Quantity of PPE supplies you have: ")
        ventilator = input("Enter the Quantity of ventilators you have seperated by comma:  ")
        oxygenator = input("Enter the Quantity of oxygenerators you have seperated by comma:  ")
        surgicals  = input("Enter the Quantity of surgicals you have:  ")
        connect = sqlite3.connect(data)
        curser = connect.cursor()
        curser.execute('''Update Personal set SANITISER = (?) where USERNAME = (?)''',(sanitiser,ID))
        curser.execute('''Update Personal set BEDS = (?) where USERNAME = (?)''',( beds,ID))
        curser.execute('''Update Personal set MASKS = (?) where USERNAME = (?)''',(Masks ,ID))
        curser.execute('''Update Personal set VITAMINC = (?) where USERNAME = (?)''',(vitamin_C,ID))
        curser.execute('''Update Personal set VITAMINB12 = (?) where USERNAME = (?)''',(vitamin_B12,ID))
        curser.execute('''Update Personal set PPE = (?) where USERNAME = (?)''',(ppe,ID))
        curser.execute('''Update Personal set VENTILATOR = (?) where USERNAME = (?)''',(ventilator,ID))
        curser.execute('''Update Personal set OXYGENERATOR = (?) where USERNAME = (?)''',(oxygenator,ID))
        curser.execute('''Update Personal set SURGICALS = (?) where USERNAME = (?)''',(surgicals ,ID))
        connect.commit()
    else:
        print("Username not Found :(  , Please Refresh the Page and Try Again")

def medical_data(data,Dict):
    ID = input("enter your current username:  ")
    if ID in Dict: 
       counter = input('''update your list in this format "item:quantity" seperated by comma :    ''')
       connect = sqlite3.connect(data)
       curser = connect.cursor()
       curser.execute('''Update Personal set DETAILS = (?) where USERNAME = (?)''',(counter,ID))
       connect.commit()

def personal_details(data,Dict):
    ID = input("enter your current username:  ")
    if ID in Dict:
      phone_number = input("Enter Your Phone Number:  ")
      address = input("Enter Your Address:    ")
      phone_number= str(phone_number)
      address  = str(address)
      connect = sqlite3.connect(data)
      curser = connect.cursor()
      #curser.execute('''REPLACE INTO  Personal (ADDRESS,PHONE) values(?,?)''',(address,phone_number))
      curser.execute('''Update Personal set ADDRESS = (?) where USERNAME = (?)''',(address,ID))
      curser.execute('''Update Personal set PHONE = (?) where USERNAME = (?)''',(phone_number,ID))
      connect.commit()
      outcome = "S"
      return outcome
    else:
        print("Wrong Username")
        outcome = "F"
        return outcome
        
def main():
    database = "Final.db"
    dataframe = read_sql(database)
    username_list, password_list,Auth = read_excel(dataframe)
    flag = 0
    
    if(flag==0):
       login = input("enter your login id:  ")
       if login in Auth:
         print("username found")
         login = str(login)
         flag = 1
       else:
         print("username not found")
         flag = -1

    if(flag == -1):
      confirm = input("Please Register to view Database(y/n):  ")  
      if(confirm == 'y'):
         Auth= update(database)
         print("Great Now Try Logging in Again")
         login = new_login(Auth)
         flag = 1
      else:
         print("Database access denied")
         flag = 0
         reset_flag = 0
         for j in range(5):
             login = new_login(Auth)
             if login in Auth:
                 flag = 1
                 break
             reset_flag +=1
             if(reset_flag ==5):
                 print("Error:To many tries Logging in , Refresh the Page and Try Again")
                 break
             
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
       confirm = input("login successful.Have you uploaded your phone number and Address?(y/n):   ")
       if(confirm=='y'):
          flag = 3
           
       else:
           o = personal_details(database,Auth)
           print(o)
           if(o=="S"):
              flag = 3
           else:
               print("phone number and address not updated,Refresh the page and Try again")

    if(flag==3):
        print("profile updated")
        update = input("Do you want to Upload or update your medical List(y/n):   ")
        if(update == 'y'):
            medical_data(database,Auth)
            flag = 4
            print("Medical Data is Successfully Updated")
        else:
            print("Medical Data Not updated")
           
           
if __name__ == "__main__":
    main()
