#  JAI SHREE RAM
import smtplib
from datetime import *
import pandas as pd

# open cvs file vai pandas 
# Reading  data from CSV file and return the data 
def read_data2():
    data = pd.read_csv("SMTP/birthdays.csv")
    return data

#  Email block 
def email(receiver_email,msg):
    # smpt server for gmail if you use different email domain check the  smpt Id
    smpt_email="smp.gmail.com"
    #dummy email not real email 
    sender_email="test@gmail.com"
    # dummy password not real password 
    password="RAJ_RAM_CHANDRA"

    with smtplib.SMTP(smpt_email) as connections:
        connections.starttls()
        connections.login(sender_email,password)
        connections.sendmail(sender_email,receiver_email,msg)
        print("Email sent successfully")

# check the birthday from data recived read_data() function that extract the from CSV file 
def check_for_BD(): 
    
    data = read_data2()
   
    today=datetime.now()
    td=today.day
    tm=today.month
    # looping through the data frame  with data.iterrows() function in row and finding the date and month and sending eamil to the person          
    for index, row in data.iterrows():
        if int(row['day']) == td and int(row['month']) == tm:
            # print(f"HBD {row['name']}! Email: {row['email']}")
            em=row['email']
            print(em)          
         
            with open("SMTP/letter_1.txt",'r') as letter1:
                read=letter1.read()
                contxt=read.replace("NAME","RAM")
                email(receiver_email=em,msg=contxt)
                




# function call 
check_for_BD()
