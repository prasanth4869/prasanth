# install connector 'pip install mysql-connector-python'
import mysql.connector as mc
con=mc.connect(host="localhost",user="root",passwd="vine96",database="pydb")
try:
    print("Successfully connected", con.connection_id)
except:
    print("Not connected")

# course object
cobj=con.cursor()

# Table creation
# q1="create table StudentDetails(id int, name varchar(20), gpa float)"
# t1=cobj.execute(q1)
# print(t1)

# Insert data
#q2="insert into StudentDetails values(%s, %s, %s)"
# r1=(101, "Katherine", 5.8)
# r2=(102, "Margott ", 6.5)
# r3=(103, "Gal Gadot", 5.6)
#
# cobj.execute(q2, r1)
# cobj.execute(q2, r2)
# cobj.execute(q2, r3)
# records=[(104, "MJ", 4.8),(105, "James", 5.9),(106, "Vikram", 7.2),(107, "Angelina", 5.3)]
# rec=cobj.executemany(q2,records)
# print("Records Updated")
# con.commit()

# READ OPERATIONS
# FETCH ALL RECORDS
# q3="select * from StudentDetails"
# cobj.execute(q3)
# res=cobj.fetchall()
# for data in res:
#     print(data)

#FETCH SINGLE RECORD
# id=102
# q4=f"select * from StudentDetails where id={id}"
# cobj.execute(q4)
# res=cobj.fetchone()
# print(res)


# UPDATE OPERATIONS
# q5="update studentdetails set gpa=7.2 where id=101"
# cobj.execute(q5)
# con.commit()

#DELETE OPERATION
q6="delete from studentdetails where id=106"
cobj.execute(q6)
con.commit()
