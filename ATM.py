
import mysql.connector as mq
from tabulate import tabulate
import stdiomask
import random

acc=None

def main():
            print("\n\n\t\t\t\t*** WELCOME    TO    MY ATM ***")
            print("\t\t\t\t=============================\n")
            print("\t\t\t\t\tMain Menu")
            print("\t\t\t\t-------------------\n")
            print("\t\t 1.Create account\t\t2.login\t\t3.Exit\n")
            
def menu():
            print("\t\t\t\tMENU")
            print("\t\t\t\t*********\n")
            print("\t\t1.DEPOSIT\t\t\t2.BANKING\n")
            print("\t\t3.BALANCE INQUERY\t\t4.SEARCH DETAILS\n")
            print("\t\t5.DELETE ACCOUT\t\t\t6.LOG OUT")

     
def  create():
     print("\t\tCreate Account")
     print("\t\t===========\n")
     nam=input("Enter your Name:")
     phn=int(input("Enter your phone no.:"))
     ob=int(input("Enter opening balance:"))
     con=mq.connect(host="localhost",user="root",passwd="root",database="bank")
     cur=con.cursor()
     pin = random.randint(1000,9999)
     query="insert into cust(name,phno,pin,balance,status)values('{}',{},{},'{}','active')". format(nam,phn,pin,ob)
     cur.execute(query)
     con.commit()
     res=cur.fetchone()
     query2="select acc_no from cust"
     cur.execute(query2)
     res=cur.fetchall()
     print("\n----------------------------------") 
     print("Your New Account no.=",res[len(res)-1][0])
     print("Your PIN is =",pin)
     print("----------------------------------\n") 
     print("Please don't share your pin with anyone")
     print("\n\tSuccussfully  Registered\n")
     con.close()
                 
def log():
         global acc
         
         l=int(input("Enter your Account no.: "))
         con=mq.connect(host="localhost",user="root",passwd="root",database="bank")
         cur=con.cursor()
         query="select * from cust where acc_no=('{}')". format(l)
         cur.execute(query)
         res= cur.fetchall()
         while res==[]:
                   print("\nYour Account no. doesn't exist,......\tTry again...\n",)
                   l=int(input("Enter your Account no.: "))

         else:
                   print("\nSuccessfully logged in\n")
                   acc=res[0][4]
         
            
def bank():
         print("\t\tCash withdrawal")
         print("\t\t=============\n")
         global acc 
         k=int(input("Enter the Amount:"))
         con=mq.connect(host="localhost",user="root",passwd="root",database="bank")
         cur=con.cursor()
         query="update cust set balance=balance-{} where acc_no={}".format(k,acc)
         cur.execute(query)
         con.commit()
         res= cur.fetchone()
         query2="insert into trans  (acc_no,amount,type) values ({},{},'withdrawn')". format(acc,k)
         cur.execute(query2)
         con.commit()
         res= cur.fetchone ()           
         print("\n",k,": Withdrawn successfully\n")
      
def dep():
         print("\t\tDeposit")
         print("\t\t======")
         global acc   
         con=mq.connect(host="localhost",user="root",passwd="root",database="bank")
         cur=con.cursor()
         a=int(input("Enter the  Amount to deposit:"))
         query="update cust set balance=balance+{} where acc_no={} ". format(a,acc)
         cur.execute(query)
         con.commit()
         res= cur.fetchone()
         query2="insert into trans  (amount,type,acc_no) values ({},'Deposit',{})". format(a,acc)
         cur.execute(query2)
         con.commit()
         res= cur.fetchone()
         print("\n",a,": Amount Deposited succussfully\n") 
         con.close()
     
def inq():
     global acc
     print("\t\tBalance inquery")
     print("\t\t============\n")
     pin=stdiomask.getpass(prompt= "Enter your 4 digit pin: ",mask='*') 
     con=mq.connect(host="localhost",user="root",passwd="root",database="bank")
     cur=con.cursor()
     query="select acc_no=({}) from cust where pin=({})". format(acc,pin)
     cur.execute(query)
     res= cur.fetchall () 
     if res==[]:
         print("\nYour Pin doesn't exist,......\tTry again...")
         pin=stdiomask.getpass(prompt= "Enter your 4 digit pin: ",mask='*') 
     else:
        query="select balance from cust where acc_no={};".format (acc)
        cur.execute(query)
        res= cur.fetchone()
        con.commit()
        print(res,": is your current balance ")
        con.close()

     
def ser():
     global acc
     print("\t\tSearch Details")
     print("\t\t==========\n")
     pin=stdiomask.getpass(prompt= "Enter your 4 digit pin: ",mask='*') 
     con=mq.connect(host="localhost",user="root",passwd="root",database="bank")
     cur=con.cursor()
     query="select acc_no=({}) from cust where pin=({})". format(acc,pin)
     cur.execute(query)
     res= cur.fetchall ()
     if res==[]:
         print("\nYour Pin doesn't exist,......\t Enter correct pin\n")
         pin=stdiomask.getpass(prompt= "Enter your 4 digit pin: ",mask='*') 
     else:
           print("\t\t1.Holder Details\n\t\t2.Transaction Details\n")
           i=int(input("Enter your choice (1 or 2):"))
           if i==1:
               query="select name,phno,status,balance from cust where acc_no={}". format(acc)
               cur.execute(query)
               res= cur.fetchall()
               print(tabulate(res,headers=[" Name "   , "  phno"," status ",  " Balance " ],tablefmt='grid' ))
           elif i==2:
               query="select type,amount,transdate from trans where acc_no={}". format(acc)
               cur.execute(query)
               res= cur.fetchall()
               print(tabulate(res,headers=["Type\t","Amount","Transdate"],tablefmt='grid'))
           else:
             print("\nEnter the correct choice:")
             i=int(input("Enter your choice (1 or 2):"))
             con.close()
     
def clo_acc():
    global acc
    a=stdiomask.getpass(prompt= "Enter your 4 digit pin: ",mask='*') 
    con= mq.connect(host='localhost', database='bank', user='root', password='root')
    cur= con.cursor()
    query ="update cust set status='N.A' where pin ={}".format(a)
    cur.execute(query)
    con.commit()
    res= cur.fetchone()
    if res==[]:
            print("\nYour Pin doesn't exist,......\tTry again...\n",)
            a=stdiomask.getpass(prompt= "Enter your 4 digit pin: ",mask='*') 
    else:
        print("\nSuccessfully Your Account closed\n")
       
while True:
         main()
         m=int(input("\nEnter  your  choice:"))
         if  m==1:
               create()
         elif m==2:
              log()
         elif m==3:
             acc=None
             print("Thankyou for visiting")
             break
         else:
            print("please choice the correct choice\n")
            m=int(input("\nEnter your choice:"))
        
         while True:
             menu()
             b=int(input("\nEnter your choice:"))
             if b==1:
                dep()
             elif b==2:
                bank()
             elif b==3:
                inq()
             elif b==4:
                ser()
             elif  b==5:
                 clo_acc()
             elif b==6:
                break
             else:
                print("please choice the correct choice\n")
                b=int(input("\nEnter your choice:"))
             p=int(input("\npress  5  to  continue...Any other key to exit...:\n"))
             if p!=5:
                break
