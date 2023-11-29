from pysqlitecipher import sqlitewrapper
# https://www.blog.letscodeofficial.com/@harshnative/encrypting-sqlite-database-in-python-using-pysqlitecipher-module-easy-and-secure-encryption-in-python-sqlite/

def createTable():
    obj = sqlitewrapper.SqliteCipher(dataBasePath="tester.db", checkSameThread=False, password=123) # make the object
    try:
        colList = [
            ["username", "TEXT"],
            ["password", "TEXT"],
            ["money", "TEXT"]
        ]
        obj.createTable("tester.db", colList, makeSecure=False, commit=True)
    except ValueError:
        pass

def addItem(item, *args):
    obj = sqlitewrapper.SqliteCipher(dataBasePath="tester.db", checkSameThread=False, password=123) # make the object
    new_row = [item, args]
    obj.insertIntoTable("tester.db", new_row, commit=True) # insert data to database

def veiw():
    obj = sqlitewrapper.SqliteCipher(dataBasePath="tester.db", checkSameThread=False, password=123) # make the object
    rows = obj.getDataFromTable("tester.db", raiseConversionError=True, omitID=False) # Get data from database
    print(rows)

def updateItem(item, columnName, newItem):
    obj = sqlitewrapper.SqliteCipher(dataBasePath="tester.db", checkSameThread=False, password=123)
    rows = obj.getDataFromTable("tester.db", raiseConversionError=True, omitID=False)
    rows = rows[1]
    ItemDic = {}  # creates the dictionary for the users to be stored in
    for row in rows:  # iterates through the database then store the values in the dictionary
        itemName = row[1]
        place = row[0]
        ItemDic[itemName] = [place]
    obj.updateInTable("tester.db", ItemDic[item][0], columnName, newItem, commit=True, raiseError=True) # Update data in database

def deleteItem(item):
    obj = sqlitewrapper.SqliteCipher(dataBasePath="tester.db", checkSameThread=False, password=123)
    rows = obj.getDataFromTable("tester.db", raiseConversionError=True, omitID=False)
    rows = rows[1]
    itemDic = {}  # creates the dictionary for the users to be stored in
    for row in rows:  # iterates through the database then store the values in the dictionary
        itemName = row[1]
        place = row[0]
        itemDic[itemName] = [place]
    obj.deleteDataInTable("tester.db", itemDic[item][0], commit=True, raiseError=True, updateId=True) # delete data from database
