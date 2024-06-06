import mysql.connector
myc = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "sboutique"
)
mycur = myc.cursor()
def check():
    query = "SELECT cust_id FROM customer"
    mycur.execute(query)
    
    id = mycur.fetchall()
    list_of_ids = [] #empty list to store extracted IDs
    for i in id: #iterate through each element in the list
        list_of_ids.append(i[0]) #appends the first element of each tuple to the list
        
    print(list_of_ids)
    
def cust_ac():
    ask = 'Y'
    list_of_ids = check() #calls the check function
    while ask in 'yY':
        cust_id = int(input("Enter your Customer ID:"))
        if cust_id in list_of_ids:
            print('This Customer ID already exists. Try creating a new one')
        else:
            c_det = () #empty tuple to store customer details
            cnam = input('First Name : ')
            clnam = input('Last Name : ')
            cphno = input('Phone Number : ')
            cadrs = input('Your Address : ')
            c_det = (cust_id, cnam, clnam, cphno, cadrs) #details to be in the tuple
            
            qry = 'INSERT INTO customer VALUES (%s, %s, %s, %s, %s, NULL)'
            value = c_det
            mycur.execute(qry, value)
            
            myc.commit()
            print('Customer details entered')
            ask = input("Do you want to continue (Y/N)")
            if ask not in ('yY'):
                space()
                break
