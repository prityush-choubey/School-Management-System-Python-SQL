import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="2001",
  database="school"
)
database = db.cursor()
admin_password="admin123"
student_password="student123"
teacher_password="teacher123"
accountant_password="accountant123"

def admission():
    admission_no=input("enter admission no")
    dob=input("enter dob")
    father_name=input("enter fathers name")
    aadhar_no =input("enter aadhar no")
    phone_no=input("enter phone no")
    address =input("enter address")
    date=input("enter date (dd-mm-yyyy):")
    clss_1=input("enter class")
    section=input("enter section")
    roll_no=input("enter rollno")
    fees=input("enter admission fees")
    sql="insert into admission values('"+admission_no+"','"+dob+"','"+father_name+"','"+aadhar_no+"','"+phone_no+"','"+address+"','"+date+"','"+clss_1+"','"+section+"','"+roll_no+"','"+fees+"')"
    database.execute(sql)
    db.commit()
    print(" new record inserted")
    


def displayadmission():
    
    admission_no=input("Enter id")
    sql="select * from admission where admission_no='"+admission_no+"'"
    database.execute(sql)
    r=database.fetchall()
    if r!=[]:
        for i in r:
            print(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10])
    else:
        print("wrong id")



def fees():
    admission_no=input("enter admission no")
    roll_no=input("enter the roll no")
    name=input("enter name")
    clss=input("enter class")
    section =input("enter section")
    month=input("enter month")
    amount=input("enter month")
    date=input("enter date (yyyy-mm-dd):")
    sql="insert into fees values('"+admission_no+"','"+roll_no+"','"+name+"','"+clss+"','"+section+"','"+month+"','"+amount+"','"+date+"')"
    database.execute(sql)
    db.commit()
    print(" new record inserted")



def displayfess():
    
    admission_no=input("Enter id")
    sql="select * from fees where admission_no='"+admission_no+"'"
    database.execute(sql)
    r=database.fetchall()
    if r!=[]:
        for i in r:
            print(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7])
    else:
        print("wrong id")



def teacher():
    id =input("enter id")
    name=input("enter name")
    phone_no=input("enter phone")
    address=input("enter add")
    salary =input("enter salary")
    sql="insert into teacher values('"+id+"','"+name+"','"+phone_no+"','"+address+"','"+salary+"')"
    database.execute(sql)
    db.commit()
    print(" new record inserted")
    
def search_teacher():
    
    id=input("Enter id")
    sql="select * from teacher where id='"+id+"'"
    database.execute(sql)
    r=database.fetchall()
    if r!=[]:
        for i in r:
            print(i[0],i[1],i[2],i[3],i[4])
    else:
        print("wrong id")

      
def class_schedule():
   period= input("enter period")
   clss= input("enter class")
   section=input("enter section")
   sub=input("enter sub")
   days=input("enter days")
   takeup=input("enter takeup")
   sql="insert into class_schedule values('"+period+"','"+clss+"','"+section+"','"+sub+"','"+days+"','"+takeup+"')"
   database.execute(sql)
   db.commit()
   print(" new record inserted")


def search_class():
    
    period=input("Enter period")
    clss=input("entter class")
    section=input("enter section")
    sql="select * from class_schedule where period='"+period+"','"+clss+"','"+section+"')"
    database.execute(sql)
    r=database.fetchall()
    if r!=[]:
        for i in r:
            print(i[0],i[1],i[2])
    else:
        print("wrong id")


def admin_menu():

  print("insert 1 to admission")
  print("insert 2 to displayadmission")
  print("insert 3 to fess")
  print("insert 4to displayfess")
  print("insert 5 to teacher")
  print("insert 6 to search_teacher")
  print("insert 7 to class_schedule")
  print("insert 8 to search_class")
  choice=input("enter choice")
  if choice=="1":
     admission()
  elif choice=="2":
     displayadmission()
  elif choice=="3":
     fees()
  elif choice=="4":
     displayfess()
  elif choice=="5":
     teacher()
  elif choice=="6":
     search_teacher()
  elif choice=="7":
     class_schedule()
  elif choice=="8":
     search_class()
  else:
     print("wrong value")

def student():
  
  print("insert 1 to displayfess")
  print("insert 2 to search_class")
  choice=input("enter choice")
  if choice=="1":
     displayfess()
  elif choice=="2":
     search_class()
  else:
     print("wrong value")

def teacher():

  print("insert 1 to search_teacher")
  print("insert 2 to class_schedule")
  print("insert 3 to search_class")
  choice=input("enter choice")
  if choice=="1":
     search_teacher()
  elif choice=="2":
     class_schedule()
  elif choice=="3":
     search_class()
  else:
     print("wrong value")

def accountant():
  
  print("insert 3 to fess")
  print("insert 4to displayfess")
  
  choice=input("enter choice")
  if choice=="1":
      fees()
  elif choice=="2":
     displayfess()
  else:
     print("wrong value")
    


while True:
  print("insert 1 for admin")
  print("insert 2 for student")
  print("insert 3 for teacher")
  print("insert 4 for accountant")
  
  choice=input("enter choice")
  if choice=="1":
    pasword=input("enter admin pasword")
    
    if pasword==admin_password:
      admin_menu()
    else:
      print("wrongpassword")
    
  elif choice=="2":
     pasword=input("enter student pasword")
    
     if pasword==student_password:
        student()
     else:
      print("wrongpassword")
  elif choice=="3":
    pasword=input("enter teacher pasword")
    
    if pasword==teacher_password:
       teacher()
    else:
       print("wrongpassword")
  elif choice=="4":
     pasword=input("enter accountant pasword")
    
     if pasword==accountant_password:
       accountant()
     else:
       print("wrongpassword")







    
    
  


               


               


