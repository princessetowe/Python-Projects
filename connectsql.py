import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "sample_db"
)
mycursor = mydb.cursor()
"""query = "SELECT COUNT(*) FROM sample_db.student_rec "
mycursor.execute(query)
result = mycursor.fetchall()
for i in result:
    print(i)
print(mycursor)"""
query2 = ("INSERT INTO sample_db.student_rec (matric_no,first_name,last_name,course, hall, graduation_year) \
    SELECT * FROM(SELECT  '20/2323', 'Tofunmi', 'Olulanke', 'CIS', 'Neal Wilson', '2022') as temp \
    WHERE NOT EXISTS \
    (SELECT matric_no FROM student_rec WHERE matric_no='20/2323') LIMIT 1")
mycursor.execute(query2)
mycursor.close()
mydb.close()

