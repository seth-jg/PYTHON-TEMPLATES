import sqlite3

def create_table():
    conn = sqlite3.connect("contacts.db") #Connecting to the table/ creating the database file if it doesnt exist
    cur = conn.cursor() # Creating the cursor to preform  sql code
    cur.execute("CREATE TABLE IF NOT EXISTS people (person TEXT, number TEXT, address TEXT)") # executing the sql code (creating the table and columns)
    conn.commit() # Making the action stay
    conn.close() # closing the table

def new_item(name, number, address):
    conn = sqlite3.connect("contacts.db") #Connecting to the table
    cur = conn.cursor() # Creating the cursor to preform  sql code
    cur.execute("INSERT INTO people VALUES (?, ?, ?)", (name, number, address)) # adding each value to each column
    conn.commit() # Making the action stay
    conn.close() # closing the table
def veiw():
    conn = sqlite3.connect("contacts.db") #Connecting to the table
    cur = conn.cursor() # Creating the cursor to preform  sql code
    cur.execute("SELECT * FROM people") # collecting all the data from table
    rows = cur.fetchall() # storing all the data in a variable
    conn.close() # closing the table

    # Store data from sql into 
    account_dic = {}
    for row in rows: # Iterates through each row 
        ac = row[0] 
        pw = row[1]
        balance = row[2]
        account_dic[ac] = [pw, balance]


def delete_contact(name):
    conn = sqlite3.connect("contacts.db") #Connecting to the table
    cur = conn.cursor() # Creating the cursor to preform  sql code
    cur.execute("DELETE FROM people WHERE person=?", (name,)) # deleting the row from the database
    conn.commit() # Making the action stay
    conn.close() # closing the table

def update_contact(name, number, address):
    conn = sqlite3.connect("contacts.db") #Connecting to the table
    cur = conn.cursor() # Creating the cursor to preform  sql code
    cur.execute("UPDATE people SET number=?, address=? WHERE person=?", (number, address, name)) # changing the rows from the selected detail
    conn.commit() # Making the action stay
    conn.close() # closing the table


# create_table()
# new_item('Seth', '01010101111', '9 Fake rd')
# update_contact('Seth', '0101101001', '9 Fake rd')


veiw()
